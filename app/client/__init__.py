from . import (
    vk_client,
    bit_client,
    yandex_click_client,
    isgd_client,
    cleanuri_client,
    relink_client
)

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

YAClickClient = yandex_click_client.YandexClickClient(
    'https://clck.ru'
)

ISGDClient = isgd_client.ISGDClient(
    'https://is.gd'
)

CleanURLClient = cleanuri_client.CleanURIClient(
    'https://cleanuri.com/'
)

RelinkClient = relink_client.RelinkClient(
    'https://rel.ink/'
)

__all__ = [
    'VKClient',
    'BITClient',
    'YAClickClient',
    'ISGDClient',
    'CleanURLClient',
    'RelinkClient'
]
