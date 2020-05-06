from typing import Optional, Union

from abc import ABCMeta, abstractmethod

import httpx
from loguru import logger


class BaseHTTPClient(metaclass=ABCMeta):

    def __init__(
            self,
            base_url: str,
            default_params: Optional[dict] = None,
            default_headers: Optional[dict] = None
    ):
        self.base_url = base_url
        self.default_params = default_params or {}
        self.default_headers = default_headers or {}

        self.http_client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.default_headers,
            params=self.default_params,
            http2=True
        )

    async def get(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None):
        custom_headers = headers or {}
        custom_params = params or {}

        logger.debug(f'Sending GET request to {url}')
        response = await self.http_client.get(url=url, params=custom_params, headers=custom_headers)
        logger.debug(f'Response return status_code: {response.status_code}, body: {response.text}')

        return response

    async def post(
            self,
            url: str,
            data: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None,
            json: Optional[dict] = None
    ):
        custom_headers = headers or {}
        custom_params = params or {}
        custom_data = data or {}
        custom_json = json or {}

        logger.debug(f'Sending POST request to {url}')
        response = await self.http_client.post(url=url, data=custom_data, params=custom_params, headers=custom_headers, json=custom_json)
        logger.debug(f'Response return status_code: {response.status_code}, body: {response.text}')

        return response

    @abstractmethod
    def _process_response(self, response: Union[dict, list]):
        raise NotImplementedError

    @abstractmethod
    async def get_short_link(self, url: str):
        raise NotImplementedError


