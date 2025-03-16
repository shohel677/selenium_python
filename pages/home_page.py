import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from abstract_components.abstract_component import AbstractComponent


class HomePage (AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)

        self.prod_link = (By.CSS_SELECTOR, "a[id='item_0_title_link']")

    def is_home_page_open(self):

        element = self.is_element_clickable(self.prod_link)
        is_product_link: bool = element.is_displayed()
        assert is_product_link is True, "Product link is not displayed. Login failed"

    def open_a_product(self):
        element = self.is_element_clickable(self.prod_link)
        element.click()