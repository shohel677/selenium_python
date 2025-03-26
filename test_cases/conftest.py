import logging
import os
import re

import pytest

from abstract_components.assertion_library import AssertionLibrary
from abstract_components.driver_master import DriverMaster
from pages.login_page import LoginPage

driver = None
assertion_html = None


@pytest.fixture(scope="function")
def instance_driver(request):
    global driver
    test_name = request.node.name  # Get the test method name
    logging.info("##############################Test started: " + test_name)
    browser_name = request.config.getoption("browser_name")

    driver = DriverMaster.browser_init(browser_name)
    request.node._driver = driver  # Attach driver to request.node for later access

    yield driver

    request.node._driver_for_report = driver


@pytest.fixture(scope="function")
def setup(instance_driver, request):
    url = request.config.getoption("url")
    username = request.config.getoption("username")
    password = request.config.getoption("password")

    instance_driver.get(url)
    instance_driver.maximize_window()
    instance_driver.implicitly_wait(10)
    login = LoginPage(instance_driver)
    login.input_username(username)
    login.input_password(password)
    login.click_submit()

    yield instance_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url", action="store", default="https://www.saucedemo.com/", help="Environment url"
    )
    parser.addoption(
        "--username", action="store", default="standard_user", help="Environment url"
    )
    parser.addoption(
        "--password", action="store", default="secret_sauce", help="Environment url"
    )


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configure logging settings for the test session."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Change to DEBUG for detailed logs

    # File handler
    file_handler = logging.FileHandler("reports/test_log.log", mode="w")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Captures and embeds a screenshot in the HTML report for every test case,
    and adds a custom full-width text banner in the report.
    """

    global assertion_html
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Determine test status and corresponding color
    if report.passed:
        test_status = "PASSED ✅"
        bg_color = "#28a745"  # Green
    elif report.failed:
        test_status = "FAILED ❌"
        bg_color = "#dc3545"  # Red
    else:
        test_status = "SKIPPED ⚠️"
        bg_color = "#ffc107"  # Yellow

    test_name = report.nodeid
    banner_html = f"""
        <div style="width: 100%; padding: 10px; background-color: {bg_color}; color: white;
                    text-align: center; font-size: 16px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;">
            Test Case: {test_name} | Status: {test_status}
        </div>
    """

    # Ensure pytest-html plugin is available
    if pytest_html:
        extra.append(pytest_html.extras.html(banner_html))

    for assertion in AssertionLibrary.get_all_assertions():
        if assertion.get_status():
            assertion_html = f"""
                     <div style="width: 100%; padding: 10px; background-color: #ffffff; color: white;
                                 text-align: left; font-size: 13px; font-weight: bold; color:black;  border-radius: 5px; margin-bottom: 10px;">
                         Pass: {assertion.get_message()}
                     </div>
                 """
        else:
            assertion_html = f"""
                                 <div style="width: 100%; padding: 10px; background-color: #ffffff; color: white;
                                             text-align: left; font-size: 13px; font-weight: bold; color:red;  border-radius: 5px; margin-bottom: 10px;">
                                     Fail : {assertion.get_message()}
                                 </div>
                             """

        # Ensure pytest-html plugin is available
        if pytest_html:
            extra.append(pytest_html.extras.html(assertion_html))

    # Run this for all test phases (setup, call, teardown)
    if report.when in ["setup", "call", "teardown"]:
        reports_dir = os.path.join(os.getcwd(), "reports/screenshots")
        os.makedirs(reports_dir, exist_ok=True)

        # Sanitize file name
        safe_test_name = re.sub(r'\W+', '_', report.nodeid)
        file_name = os.path.join(reports_dir, f"{safe_test_name}.png")

        _capture_screenshot(file_name, item)

        # Embed screenshot in the HTML report
        if os.path.exists(file_name) and pytest_html:
            html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                   f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))

    report.extras = extra
    AssertionLibrary.get_all_assertions().clear()
    # 🔴 Close WebDriver after reporting is complete
    get_driver = getattr(item, "_driver_for_report", None)
    if get_driver:
        try:
            get_driver.quit()
            logging.info("WebDriver closed successfully.")
        except Exception as e:
            logging.error(f"Error while closing WebDriver: {e}")


def _capture_screenshot(file_name, item):
    """
    Captures a screenshot using Selenium WebDriver.
    Fetches the driver instance dynamically from 'item' to avoid issues with global variables.
    """
    get_driver = getattr(item, "funcargs", {}).get("instance_driver", None)
    if get_driver:
        try:
            get_driver.get_screenshot_as_file(file_name)
            logging.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            logging.error(f"Failed to capture screenshot: {e}")
    else:
        logging.warning("WebDriver instance is not available for capturing screenshot.")
