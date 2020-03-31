from aiogram.dispatcher import FSMContext

from client import *
from middlewares.i18n import i18n

CLIENTS = {
    str(VKClient): VKClient,
    str(BITClient): BITClient,
    str(YAClickClient): YAClickClient,
    str(ISGDClient): ISGDClient
}


async def get_client(state: FSMContext):
    async with state.proxy() as data:
        return CLIENTS[data.get('shortener', 'vk.cc')]


async def get_lang(state: FSMContext):
    async with state.proxy() as data:
        return i18n.AVAILABLE_LANGUAGES[data.get('locale')].title
