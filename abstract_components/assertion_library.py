import logging


class AssertionLibrary:
    assertion_results = []

    @staticmethod
    def should_be_true(condition: bool, expected: str, actual: str):
        if condition:
            logging.critical(f"Pass: {expected}")
            AssertionLibrary.assertion_results.append(AssertionLibrary.AssertionInfo(True, expected))
            assert True, expected
        else:
            logging.critical(f"Fail: {actual}")
            AssertionLibrary.assertion_results.append(AssertionLibrary.AssertionInfo(False, expected))
            assert False, actual

    @staticmethod
    def get_all_assertions():
        return AssertionLibrary.assertion_results

    class AssertionInfo:
        def __init__(self, status: bool, message: str):
            self.status = status
            self.message = message

        def get_status(self):
            return self.status

        def get_message(self):
            return self.message
