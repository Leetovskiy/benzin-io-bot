"""Benzin.io API class"""

import requests


class BenzinAPI:
    def __init__(self, api_key: str) -> None:
        self.API_KEY: str = api_key
        self.API_URL = 'https://api.benzin.io/v1/removeBackground'

    def _send_request(self, headers: dict = None, **parameters) -> requests.Response:
        """Send POST-request to Benzin.io

        Args:
            **parameters:
                Request parameters. See available parameters list at
                https://benzin.io/integration/api-docs/
        """
        if headers is None:
            headers = {}
        headers.update({'X-Api-Key': self.API_KEY})

        response = requests.post(self.API_URL, headers=headers, data=parameters)
        return response

    def upload_by_url(self, url, **parameters):
        """Send image URL and get response"""
        response = self._send_request(image_file_url=url, **parameters)
        return response
