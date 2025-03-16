from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent
from pages.checkout_page import CheckoutPage


class ProductPage(AbstractComponent):
    product_details_img = (By.XPATH, "//img[@class='inventory_details_img']")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    remove_button = (By.XPATH, "//button[text()='Remove']")
    cart_icon = (By.XPATH, "//a/span[text()='1']")

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_page = CheckoutPage(driver)

    def product_details_page_displayed(self):
        is_product_details_page: bool = self.driver.find_element(*self.product_details_img).is_displayed()
        assert is_product_details_page, "Product details page is not displayed"

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        self.driver.find_element(*self.remove_button).is_displayed()

    def product_added_to_cart(self):
        added_number = self.driver.find_element(*self.cart_icon).text
        assert added_number == "1", "Product is not added in cart"

    def go_to_checkout_page(self):
        self.driver.find_element(*self.cart_icon).click()
        return self.checkout_page
