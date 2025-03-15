import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage


class TestSauceDemo:

    def test_to_validate_login(self, setup, instance_driver):
        home_page = HomePage(instance_driver)
        home_page.is_home_page_open()



    def test_to_validate_login2(self, setup, instance_driver):

        wait = WebDriverWait(instance_driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[id='item_0_title_link']")))
        setup.find_element(By.CSS_SELECTOR, "a[id='item_0_title_link']").click()
        time.sleep(2)