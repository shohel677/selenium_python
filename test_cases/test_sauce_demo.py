import pytest

from pages.home_page import HomePage


class TestSauceDemo:
    @pytest.mark.regression
    def test_to_validate_login(self, setup, instance_driver):
        home_page = HomePage(instance_driver)
        home_page.is_home_page_open()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_to_open_a_product(self, setup, instance_driver):
        home_page = HomePage(instance_driver)
        home_page.is_home_page_open()
        product_detail_page = home_page.open_a_product()
        product_detail_page.product_details_page_displayed()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_to_add_a_product_in_cart(self, setup, instance_driver):
        home_page = HomePage(instance_driver)
        home_page.is_home_page_open()
        product_detail_page = home_page.open_a_product()
        product_detail_page.product_details_page_displayed()
        product_detail_page.click_add_to_cart()
        product_detail_page.product_added_to_cart()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_to_checkout_a_product(self, setup, instance_driver):
        home_page = HomePage(instance_driver)
        home_page.is_home_page_open()
        product_detail_page = home_page.open_a_product()
        product_detail_page.product_details_page_displayed()
        product_detail_page.click_add_to_cart()
        product_detail_page.product_added_to_cart()
        checkout_page = product_detail_page.go_to_checkout_page()
        checkout_page.click_checkout_button()
        checkout_page.enter_firstname()
        checkout_page.enter_lastname()
        checkout_page.enter_zip_code()
        checkout_page.click_submit_button()

