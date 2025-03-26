from selenium.webdriver.common.by import By

from abstract_components.abstract_component import AbstractComponent
from app_elements.app_components.button import Button
from app_elements.app_components.image import Image
from pages.checkout_page import CheckoutPage


class ProductPage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_page = CheckoutPage(driver)
        self.product_details_img = Image(driver, (By.XPATH, "//img[@class='inventory_details_img']"),
                                         "Image in product details page")
        self.add_to_cart_button = Button(driver, (By.XPATH, "//button[text()='Add to cart']"),
                                         "Add to cart button in product page")
        self.remove_button = Button(driver, (By.XPATH, "//button[text()='Remove']"), "Remove button in product page")
        self.cart_icon = Button(driver, (By.XPATH, "//a/span[text()='1']"), "Cart icon")

    def product_details_page_displayed(self):
        is_product_details_page: bool = self.product_details_img.is_shown()
        assert is_product_details_page, "Product details page is not displayed"

    def click_add_to_cart(self):
        self.add_to_cart_button.selenium_click()
        self.remove_button.is_shown()

    def product_added_to_cart(self):
        added_number = self.cart_icon.get_text()
        assert added_number == "1", "Product is not added in cart"

    def go_to_checkout_page(self):
        self.cart_icon.selenium_click()
        return self.checkout_page
