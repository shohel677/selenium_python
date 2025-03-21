
from app_elements.app_element import AppElement


class Button(AppElement):
    def __init__(self, driver, element_or_locator, name: str):
        super().__init__(driver, element_or_locator, name)
