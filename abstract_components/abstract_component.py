import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AbstractComponent:
    def __init__(self, driver):
        self.driver = driver
        # Initialize logger for this page
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set log level (INFO, DEBUG, etc.)

    def clickable_state_of_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        self.logger.info("Checking click ability of element: " + locator[1])
        return wait.until(expected_conditions.element_to_be_clickable(locator))

    def presence_of_element(self, locator: tuple, time_in_seconds: int = 10):
        wait = WebDriverWait(self.driver, time_in_seconds)
        self.logger.info("Checking presence of element: " + locator[1])
        return wait.until(expected_conditions.presence_of_element_located(locator))
