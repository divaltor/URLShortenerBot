from .http_client import BaseHTTPClient

from typing import Optional

from loguru import logger


class BITClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'bit.ly'

    def _process_response(self, response: Optional[dict] = None):
        if response is None or response.get('message'):
            logger.error(f'Error message of response: {response["message"]}. Error code: {response.get("description")}')
            return None

        return response['link']

    async def get_short_link(self, url: str):
        response = await self.post('/v4/shorten', json={'long_url': url})

        return self._process_response(response.json())
