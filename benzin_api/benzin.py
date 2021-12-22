"""Benzin.io API class"""

from aiohttp import ClientSession

from .exceptions import UnspecifiedToken


class BenzinAPI:
    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise UnspecifiedToken
        elif not isinstance(api_key, str):
            raise TypeError

        self.API_KEY: str = api_key
        self.API_URL: str = 'https://api.benzin.io/v1/removeBackground'

    async def _send_request(self, headers: dict = None, **parameters) -> dict:
        """Send POST-request to Benzin.io

        Args:
            headers: HTTP-request headers exclude API token. It will be passed
                automatically
            **parameters: HTTP-request parameters. See available list at
                https://benzin.io/integration/api-docs/

        Returns:
            Deserialized JSON of response

        Raises:
            ClientResponseError: if response status code is 400 and greater
        """
        if headers is None:
            headers = {}
        headers.update({'X-Api-Key': self.API_KEY})
        if 'output_format' not in parameters:
            parameters.update({'output_format': 'json'})

        async with ClientSession() as session:
            async with session.post(self.API_URL, headers=headers, data=parameters) as response:
                response.raise_for_status()
                return await response.json()

    async def remove_background_by_url(self, url, **parameters) -> dict:
        """Send image by URL and get result response"""
        response = await self._send_request(image_file_url=url, **parameters)
        return response
