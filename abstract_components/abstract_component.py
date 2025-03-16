from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AbstractComponent:
    def __init__(self, driver):
        self.driver = driver

    def is_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located(locator))
