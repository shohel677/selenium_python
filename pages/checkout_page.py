from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent
from app_elements.app_components.button import Button
from app_elements.app_components.input import Input


class CheckoutPage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = Button(driver, (By.XPATH, "//button[@id='checkout']"), "Checkout button")
        self.submit_button = Button(driver, (By.XPATH, "//input[@type='submit']"), "Submit button")
        self.firstname = Input(driver, (By.XPATH, "//input[@placeholder='First Name']"), "First name")
        self.lastname = Input(driver, (By.XPATH, "//input[@placeholder='Last Name']"), "Last name")
        self.zip_code = Input(driver, (By.XPATH, "//input[@placeholder='Zip/Postal Code']"), "Zip code")

    def click_checkout_button(self):
        self.checkout_button.selenium_click()

    def enter_firstname(self):
        self.presence_of_element((By.XPATH, "//input[@placeholder='First Name']"))
        self.firstname.type("Golzar")

    def enter_lastname(self):
        self.lastname.type("Shohel")

    def enter_zip_code(self):
        self.zip_code.type("1216")

    def click_submit_button(self):
        self.submit_button.selenium_click()
