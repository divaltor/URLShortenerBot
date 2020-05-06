from aiogram.dispatcher import FSMContext

from app.client import VKClient, BITClient, YAClickClient, ISGDClient, CleanURLClient, RelinkClient
from app.client.http_client import BaseHTTPClient
from app.middlewares.i18n import i18n

WRONG_CHARS = {
    '&amp;': '',
    ' ': '%20'
}

CLIENTS = {
    str(VKClient): VKClient,
    str(BITClient): BITClient,
    str(YAClickClient): YAClickClient,
    str(ISGDClient): ISGDClient,
    str(CleanURLClient): CleanURLClient,
    str(RelinkClient): RelinkClient
}


async def get_client(state: FSMContext) -> BaseHTTPClient:
    async with state.proxy() as data:
        return CLIENTS[data.get('shortener', 'vk.cc')]


async def get_lang(state: FSMContext) -> str:
    async with state.proxy() as data:
        return i18n.AVAILABLE_LANGUAGES[data.get('locale')].title


def translate_chars(text: str) -> str:
    for item, value in WRONG_CHARS.items():
        text = text.replace(item, value)

    return text
