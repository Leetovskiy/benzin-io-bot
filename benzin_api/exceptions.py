"""Benzin API exceptions"""


class BenzinException(BaseException):
    """Base Benzin API exception"""

    def __init__(self, message: str = None):
        if message is None:
            message = 'Invalid request parameters or the input image could not be processed'

        self.message = message
        super().__init__(self.message)


class UnspecifiedToken(BenzinException):
    """Token is not specified"""

    def __init__(self, message: str = None):
        if message is None:
            message = 'Token is not specified'

        self.message = message
        super().__init__(self.message)
