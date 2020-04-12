from .http_client import BaseHTTPClient

from typing import Optional

from loguru import logger


class RelinkClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'rel.ink'

    def _process_response(self, response: Optional[dict, list]):
        if response and isinstance(response.get('url'), list):
            logger.error(f'Error message of response: {response["url"]}')
            return

        return f'https://rel.ink/{response["hashid"]}'

    async def get_short_link(self, url: str):
        response = await self.post('/api/links/', data={'url': url})

        return self._process_response(response.json())
