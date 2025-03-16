from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent


class LoginPage(AbstractComponent):
    username_field = (By.ID, "user-name")
    password_field = (By.NAME, "password")
    submit_button = (By.CSS_SELECTOR, "input#login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
