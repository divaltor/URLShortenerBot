from .http_client import BaseHTTPClient

from typing import Optional, Union

from loguru import logger


class CleanURIClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'cleanuri.com'

    def _process_response(self, response: Union[list, dict]) -> Optional[str]:
        if isinstance(response, list):
            return None

        if response and response.get('error'):
            logger.error(f'Error message of response: {response["error"]}')
            return None

        return response['result_url']

    async def get_short_link(self, url: str) -> Optional[str]:
        response = await self.post('/api/v1/shorten', data={'url': url})

        return self._process_response(response.json())
