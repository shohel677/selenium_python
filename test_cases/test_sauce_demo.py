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
        home_page.open_a_product()
