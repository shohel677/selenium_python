import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def instance_driver(request):
    browser_name = request.config.getoption("browser_name")

    if "chrome" in browser_name:
        options = webdriver.ChromeOptions()
        if browser_name == "chromeheadless":
            options.add_argument("--headless")  # Run Chrome in headless mode
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")  # Optional: Set screen size
            driver = webdriver.Chrome(options=options)
        else:
            options.add_experimental_option("detach", True)  # Prevents browser from closing automatically
            driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver

    print("\nClosing the browser after test execution")
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
    (login.input_username(username).
     input_password(password)
     .click_submit())

    yield instance_driver  # Keeps the driver alive for the test


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
