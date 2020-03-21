from . import vk_client, bit_client

import config

VK_PARAMS = {
    'v': config.API_VERSION,
    'access_token': config.SERVICE_TOKEN
}

VKClient = vk_client.VKClient(
    'https://api.vk.com',
    default_params=VK_PARAMS
)

BIT_HEADERS = {
    'Authorization': f'Bearer {config.BIT_TOKEN}',
    'Host': 'api-ssl.bitly.com',
    'Content-Type': 'application/json'
}

if config.ENABLED_CLIENTS['BIT']:
    BITClient = http_client.HTTPClient(
        'https://api-ssl.bitly.com',
        default_headers=BIT_HEADERS
    )

__all__ = ['VKClient', 'BITClient']