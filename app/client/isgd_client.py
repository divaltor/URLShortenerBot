from .http_client import BaseHTTPClient

from typing import Optional, Union

from loguru import logger


class ISGDClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'is.gd'

    def _process_response(self, response: Union[list, dict]) -> Optional[str]:
        if isinstance(response, list):
            return None

        if response and response.get('errorcode'):
            logger.error(f'Error message of response: {response["errormessage"]}. Error code: {response["errorcode"]}')
            return None

        return response['shorturl']

    async def get_short_link(self, url: str) -> Optional[str]:
        response = await self.get('/create.php', params={
            'format': 'json',
            'url': url
        })

        return self._process_response(response.json())
