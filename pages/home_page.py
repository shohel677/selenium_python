import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from abstract_components.abstract_component import AbstractComponent
from app_elements.app_components.label import Label
from app_elements.app_components.select_dropdown import SelectDropdown
from pages.product_page import ProductPage


class HomePage(AbstractComponent):
    product: tuple = (By.XPATH, "//div[text()='Sauce Labs Backpack']/parent::a")

    def __init__(self, driver):
        super().__init__(driver)
        self.product_page = ProductPage(driver)
        self.product_button = Label(driver, (By.XPATH, "//div[text()='Sauce Labs Backpack']/parent::a"),
                                    "Product button")
        self.price_sort = SelectDropdown(driver, (By.XPATH, "//select"), "Price sorting")

    def is_home_page_open(self):
        element = self.presence_of_element(self.product)
        is_product_link: bool = element.is_displayed()
        assert is_product_link is True, "Product link is not displayed. Login failed"

    def open_a_product(self):
        self.product_button.selenium_click()
        return self.product_page

    def sort_product_by_price(self):
        """Sort products by price and handle stale element issues."""
        self.price_sort.select_option_by_value("za")

        # Ensure the dropdown is still shown after selection
        self.price_sort.is_shown()

        # Wait for the page to update instead of using time.sleep
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of(self.product_button.get_wrapped_element())
        )

        for _ in range(3):  # Retry up to 3 times in case of stale reference
            try:
                # Re-locate the dropdown element
                dropdown_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of(self.price_sort.get_wrapped_element())  # Replace with actual dropdown ID
                )

                # Re-initialize the SelectHandler with the new dropdown element
                self.price_sort = SelectDropdown(self.driver, dropdown_element, "Price sorting")

                # Get the selected option
                selected_option = self.price_sort.get_first_selected_option()
                break  # Exit loop if successful
            except StaleElementReferenceException:
                print("Dropdown became stale. Retrying...")

