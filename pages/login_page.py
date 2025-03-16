from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent


class LoginPage (AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
