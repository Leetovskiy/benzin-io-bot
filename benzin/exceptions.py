# Copyright © 2022 Vitaliy Zaitsev. All rights reserved.
# Contacts: dev.zaitsev@gmail.com
# Licensed under the Apache License, Version 2.0
"""BenzinAPI exceptions"""


class ResponseError(Exception):
    """Exception raised in cases when API returned an error

    Attributes:
        message (str): exception message
        status (int): response status code
        reason (str: response error reason
    """

    def __init__(self, status: int, reason: str):
        message = f'{status}, {reason}'
        self.message: str = message
        self.status: int = status
        self.reason: str = reason
        super().__init__(self.message)

    def __str__(self):
        return str(self.message)
