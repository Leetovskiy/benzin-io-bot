"""Benzin.io API class"""

from aiohttp import ClientSession


class BenzinAPI:
    def __init__(self, api_key: str) -> None:
        self.API_KEY: str = api_key
        self.API_URL = 'https://api.benzin.io/v1/removeBackground'

    async def _send_request(self, headers: dict = None, **parameters) -> dict:
        """Send POST-request to Benzin.io

        Args:
            **parameters:
                Request parameters. See available parameters list at
                https://benzin.io/integration/api-docs/

        Returns:
            Deserialized JSON
        """
        if headers is None:
            headers = {}
        headers.update({'X-Api-Key': self.API_KEY})
        if 'output_format' not in parameters:
            parameters.update({'output_format': 'json'})

        async with ClientSession() as session:
            async with session.post(self.API_URL, headers=headers, data=parameters) as response:
                return await response.json()

    async def remove_background_by_url(self, url, **parameters) -> dict:
        """Send image by URL and get result response"""
        response = await self._send_request(image_file_url=url, **parameters)
        return response
