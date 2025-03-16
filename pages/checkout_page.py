from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent


class CheckoutPage(AbstractComponent):
    checkout_button = (By.XPATH, "//button[@id='checkout']")
    firstname = (By.XPATH, "//input[@placeholder='First Name']")
    lastname = (By.XPATH, "//input[@placeholder='Last Name']")
    zip_code = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
    submit_button = (By.XPATH, "//input[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_firstname(self):
        self.presence_of_element(self.firstname).send_keys("Golzar")

    def enter_lastname(self):
        self.driver.find_element(*self.lastname).send_keys("Shohel")

    def enter_zip_code(self):
        self.driver.find_element(*self.zip_code).send_keys("1216")

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()
