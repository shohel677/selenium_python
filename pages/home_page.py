import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.prod_link = (By.CSS_SELECTOR, "a[id='item_0_title_link']")

    def is_home_page_open(self):
        wait = WebDriverWait(self.driver, 10)
        product_link = wait.until(expected_conditions.presence_of_element_located(self.prod_link))
        is_product_link: bool = product_link.is_displayed()
        assert is_product_link is True, "Product link is not displayed. Login failed"

    def open_a_product(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.prod_link)).click()
