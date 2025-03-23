import logging

from selenium.webdriver.support.select import Select

from app_elements.app_element import AppElement


class SelectDropdown(AppElement):
    def __init__(self, driver, element_or_locator, name: str):
        super().__init__(driver, element_or_locator, name)
        self.select = Select(self.get_wrapped_element())

    def select_option_by_index(self, index):
        if isinstance(index, int):
            self.logger.info(f"Selecting option by index: {index}")
            self.select.select_by_index(index)
        elif isinstance(index, list):
            for ind in index:
                self.logger.info(f"Selecting option by index: {ind}")
                self.select.select_by_index(ind)

    def select_option_by_visible_text(self, visible_text):
        if isinstance(visible_text, str):
            self.logger.info(f"Selecting option by visible text: {visible_text}")
            self.select.select_by_visible_text(visible_text)
        elif isinstance(visible_text, list):
            for text in visible_text:
                self.logger.info(f"Selecting option by visible text: {text}")
                self.select.select_by_visible_text(text)

    def select_option_by_value(self, value: str):
        if isinstance(value, str):
            self.logger.info(f"Selecting option by value: {value}")
            self.select.select_by_value(value)
        elif isinstance(value, list):
            for val in value:
                self.logger.info(f"Selecting option by value: {val}")
                self.select.select_by_value(val)

    def get_first_selected_option(self) -> str:
        option_selected = self.select.first_selected_option.text
        self.logger.info(f"First selected option: {option_selected}")
        return option_selected

    def get_all_selected_option(self):
        options_selected = [option.text for option in self.select.all_selected_options]
        self.logger.info(f"All selected option: {options_selected}")
        return options_selected
