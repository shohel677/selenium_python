
from app_elements.app_element import AppElement


class Image(AppElement):
    def __init__(self, driver, element_or_locator, name: str):
        super().__init__(driver, element_or_locator, name)
