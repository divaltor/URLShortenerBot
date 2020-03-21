from .http_client import BaseHTTPClient

from urllib.parse import quote

from typing import Optional


class YandexClickClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'clck.ru'

    def _process_response(self, response: Optional[dict] = None):
        pass

    async def get_short_link(self, url: str):
        response = await self.get('/--', params={'url': quote(url)})

        return response.text
