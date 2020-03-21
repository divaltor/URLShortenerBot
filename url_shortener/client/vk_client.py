from .http_client import BaseHTTPClient

from typing import Optional

from loguru import logger


class VKClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'VK'

    def _process_response(self, response: Optional[dict] = None):
        if response is None or response.get('error'):
            logger.error(f'Error message of response: {response["error"]["error_msg"]}. Error code: {response["error"]["error_code"]}')
            return None

        return response['response']['short_url']

    async def get_short_link(self, url: str):
        response = await self.get('/method/utils.getShortLink', params={'url': url})

        return self._process_response(response.json())
