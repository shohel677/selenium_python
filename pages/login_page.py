from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        return self

    def input_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)
        return self

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
        return HomePage(self.driver)
