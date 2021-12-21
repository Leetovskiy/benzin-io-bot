"""Benzin.io API class"""

from aiohttp import ClientSession

from .exceptions import BenzinException, MissingImage, UnspecifiedToken


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
            Deserialized JSON

        Raises:
            MissingImage: If server return "missing image" error
            BenzinException: In any another case when server return error
        """
        if headers is None:
            headers = {}
        headers.update({'X-Api-Key': self.API_KEY})
        if 'output_format' not in parameters:
            parameters.update({'output_format': 'json'})

        async with ClientSession() as session:
            async with session.post(self.API_URL, headers=headers, data=parameters) as response:
                response_json = await response.json()

                if response.status != 200:
                    if response_json['error'] == 'missing image':
                        raise MissingImage
                    else:
                        raise BenzinException
                return response_json

    async def remove_background_by_url(self, url, **parameters) -> dict:
        """Send image by URL and get result response"""
        response = await self._send_request(image_file_url=url, **parameters)
        return response
