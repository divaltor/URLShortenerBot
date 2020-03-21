from .http_client import BaseHTTPClient

from typing import Optional


class BITClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def process_response(self, response):
        pass

    def get_short_link(self, url):
        pass
