import logging

import pytest
from selenium import webdriver

from abstract_components.driver_master import DriverMaster
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def instance_driver(request):
    test_name = request.node.name  # Get the test method name
    logging.info("##############################Test started: " + test_name)
    browser_name = request.config.getoption("browser_name")

    driver = DriverMaster.browser_init(browser_name)

    yield driver

    logging.info("")

    driver.quit()


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
    file_handler = logging.FileHandler("../reports/log/test_log.log", mode="w")
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


def get_driver_instance():
    return driver
