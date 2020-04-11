from .http_client import BaseHTTPClient

from typing import Optional

from loguru import logger


class ISGDClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'is.gd'

    def _process_response(self, response: Optional[dict] = None):
        if response is None or response.get('errorcode'):
            logger.error(f'Error message of response: {response["errormessage"]}. Error code: {response["errorcode"]}')
            return

        return response['shorturl']

    async def get_short_link(self, url: str):
        response = await self.get('/create.php', params={
            'format': 'json',
            'url': url
        })

        return self._process_response(response.json())
