from . import vk_client, bit_client

import config

VKClient = vk_client.VKClient(
    'https://api.vk.com',
    default_params={
        'v': config.API_VERSION,
        'access_token': config.SERVICE_TOKEN
    }
)

if config.ENABLED_CLIENTS['BIT']:
    BITClient = http_client.HTTPClient(
        'https://api-ssl.bitly.com',
        default_headers=BIT_HEADERS
    )

__all__ = ['VKClient', 'BITClient']