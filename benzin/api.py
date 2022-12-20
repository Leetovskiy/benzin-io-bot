# Copyright © 2022 Vitaliy Zaitsev. All rights reserved.
# Contacts: dev.zaitsev@gmail.com
# Licensed under the Apache License, Version 2.0
"""Benzin.io API classes"""

from typing import Mapping, Iterable, Union, Any, Optional, Dict

from aiohttp import FormData, ClientSession, ClientResponse
from aiohttp.typedefs import LooseHeaders

from .exceptions import ResponseError


class BenzinAPI:
    """BenzinAPI requests

    Attributes:
        API_URL (str): Actual URL for reaching the Benzin API
    """

    API_URL = 'https://api.benzin.io/v1/removeBackground'

    @classmethod
    async def request(
            cls,
            method: str,
            params: Optional[Mapping[str, str]] = None,
            data: Optional[Union[FormData, Iterable[Any]]] = None,
            headers: Optional[LooseHeaders] = None
    ) -> Union[Dict[str, Any], ClientResponse]:
        """Send a request to the API

        All arguments are similar to aiohttp request method

        Args:
            method: HTTP-method: 'GET' or 'POST' (case-sensitive)
            params: Request parameters
            data: Request data
            headers: Request headers

        Returns:
            JSON-serialized dict or ClientResponse object

        Raises:
            ResponseError: If the response status code is 400 or greater
        """
        url = cls.API_URL

        async with ClientSession() as session:
            async with session.request(method,
                                       url,
                                       params=params,
                                       data=data,
                                       headers=headers) as response:
                if not response.ok:
                    status, reason = response.status, response.reason
                    raise ResponseError(status, reason)

                if response.content_type == 'application/json':
                    return await response.json()
                return response

    @classmethod
    async def post(cls,
                   params: Optional[Mapping[str, str]] = None,
                   data: Optional[Union[FormData, Iterable[Any]]] = None,
                   headers: Optional[LooseHeaders] = None) -> Any:
        """Perform a POST-request to the API

        Just an alias of the BenzinAPI.request method, so all the
        arguments are similar.
        """
        return await cls.request('POST', headers=headers, data=data, params=params)


class Benzin:
    """Wrapping over raw API requests

    Attributes:
        token (str): Benzin API token
    """

    def __init__(self, api_token: str) -> None:
        """Initialization

        Args:
            api_token (str): Benzin API token
        """
        if not isinstance(api_token, str):
            raise TypeError('api_token should be a string')

        self.token = api_token

    async def remove_background(
            self,
            image_file_b64: Optional[str] = None,
            image_file_url: Optional[str] = None,
            size: str = 'preview',
            channels: str = 'rgba',
            output_format: str = 'image',
            crop: bool = False,
            crop_margin: Optional[str] = None,
            bg_color: Optional[str] = None,
            bg_image_file_b64: Optional[str] = None,
            bg_image_file_url: Optional[str] = None
    ) -> Union[Dict[str, Any], ClientResponse]:
        """Remove the background from any image

        It is required to pass at least one of the parameters: image_file_b64,
        image_file_url.

        The parameters are similar to those described in the Benzin API
        documentation (excluding image_file, it will be soon, hopefully)

        Returns:
            JSON-serialized dict or ClientResponse object
        """
        values = locals().copy()
        values.pop('self')
        parameters = {
            key: str(value)
            for key, value in values.items()
            if value is not None
        }
        response = await BenzinAPI.post(
            headers={'X-Api-Key': self.token},
            data=parameters)
        return response
