from .http_client import BaseHTTPClient

from typing import Optional
from urllib.parse import quote

from loguru import logger


class CleanURIClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'cleanuri.com'

    def _process_response(self, response: Optional[dict] = None):
        if response is None or response.get('error'):
            logger.error(f'Error message of response: {response["error"]}')
            return

        return response['result_url']

    async def get_short_link(self, url: str):
        logger.info(url)
        logger.info(quote(url))
        response = await self.post('/api/v1/shorten', data={'url': url})

        return self._process_response(response.json())
