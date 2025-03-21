
from app_elements.app_element import AppElement


class Input(AppElement):
    def __init__(self, driver, element_or_locator, name: str):
        super().__init__(driver, element_or_locator, name)

    def type(self, type_text):
        self.logger.info("Typing text on " + self.get_name() + ": " + type_text  )
        self.get_wrapped_element().send_keys(type_text)
