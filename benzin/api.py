"""Benzin.io API classes"""

from typing import Mapping, Iterable, Union, Any, Optional

from aiohttp import FormData, ClientSession
from aiohttp.typedefs import LooseHeaders

from .exceptions import ResponseError


class BenzinAPI:
    """BenzinAPI requests

    Attributes:
        API_URL (str): Actual URL for reaching the Benzin API
    """

    API_URL = 'https://api.benzin.io/v1/removeBackground'

    @classmethod
    async def request(cls,
                      method: str,
                      params: Optional[Mapping[str, str]] = None,
                      data: Optional[Union[FormData, Iterable[Any]]] = None,
                      headers: Optional[LooseHeaders] = None) -> Any:
        """Send a request to the API

        All arguments are similar to aiohttp request method

        Args:
            method: HTTP-method: 'GET' or 'POST' (case-sensitive)
            params: Request parameters
            data: Request data
            headers: Request headers

        Returns:
            aiohttp-response object

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
        return cls.request('POST', headers=headers, data=data, params=params)
