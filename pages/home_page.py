import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def is_home_page_open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[id='item_0_title_link']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[id='item_0_title_link']").click()
        time.sleep(2)
