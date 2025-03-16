import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from abstract_components.abstract_component import AbstractComponent
from pages.product_page import ProductPage


class HomePage(AbstractComponent):
    product = (By.XPATH, "//div[text()='Sauce Labs Backpack']/parent::a")

    def __init__(self, driver):
        super().__init__(driver)
        self.product_page = ProductPage(driver)

    def is_home_page_open(self):
        element = self.presence_of_element(self.product)
        is_product_link: bool = element.is_displayed()
        assert is_product_link is True, "Product link is not displayed. Login failed"

    def open_a_product(self):
        element = self.clickable_state_of_element(self.product)
        element.click()
        return self.product_page
