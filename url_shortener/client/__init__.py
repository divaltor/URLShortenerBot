from . import vk_client, bit_client

import config

VKClient = vk_client.VKClient(
    'https://api.vk.com',
    default_params={
        'v': config.API_VERSION,
        'access_token': config.SERVICE_TOKEN
    }
)

BITClient = bit_client.BITClient(
    'https://api-ssl.bitly.com',
    default_headers={
        'Authorization': f'Bearer {config.BIT_TOKEN}',
        'Host': 'api-ssl.bitly.com',
        'Content-Type': 'application/json'
    }
)

__all__ = ['VKClient', 'BITClient']
