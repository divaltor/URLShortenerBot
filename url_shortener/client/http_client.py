from typing import Optional

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

        logger.debug(f'Sending request to {url}')
        response = await self.http_client.get(url=url, params=custom_params, headers=custom_headers)
        logger.debug(f'Response return status_code: {response.status_code}, body: {response.text}')

        return response

    @abstractmethod
    def process_response(self, response):
        pass

    @abstractmethod
    def get_short_link(self, url):
        pass


