
class ExceptionVKAPIRequest(Exception):
    """A class of errors that may occur when working with VK API"""
    errors = {
        1: "An unknown error has occurred.",
        3: "An unknown API method was passed.",
        5: "User authorization failed. Check the token.",
        100: "One of the required parameters was not passed or was passed in the wrong format."
    }

    def __init__(self, error_code):
        self.error = self.errors.get(error_code)

    def __str__(self):
        msg = self.error if self.error else "Unknown error"
        return f"An error occurred while accessing the VK API: {msg}"

