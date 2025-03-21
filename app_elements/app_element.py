import logging

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from abstract_components.abstract_component import AbstractComponent
from test_cases.conftest import instance_driver, get_driver_instance


class AppElement:
    POLLING = 30

    IMPLICIT = 0

    def __init__(self, driver, element_or_locator=None, name: str = None):
        self.driver = driver
        self.name = name
        self.element = None  # Ensure `self.element` exists
        self.locator = None  # Ensure `self.locator` exists

        if isinstance(element_or_locator, (WebElement, type(None))):
            self.element = element_or_locator
        elif isinstance(element_or_locator, (tuple, type(None))):
            self.locator = element_or_locator
        else:
            raise ValueError("Expected WebElement, locator tuple, or None")
            # Initialize logger for this page
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set log level (INFO, DEBUG, etc.)

    def get_name(self):
        return self.name

    def get_wrapped_element(self) -> WebElement:
        if self.element:
            return self.element
        to_return = self.c_find_element(10)

        if to_return is None:
            raise NoSuchElementException("Element not found")

        return to_return

    def c_find_element(self, timeout_in_seconds: int):
        """Waits for the element using Fluent Wait and returns it."""

        # Temporarily disable implicit wait
        self.driver.implicitly_wait(0)

        try:

            element = self.driver.find_element(*self.locator)

            if element:
                return element
            else:
                raise Exception(f"Element {self.name} is not found")

        finally:
            # Restore implicit wait
            self.driver.implicitly_wait(self.IMPLICIT)

    def selenium_click(self):
        self.logger.info("clicking element: " + self.get_name())
        self.get_wrapped_element().click()


