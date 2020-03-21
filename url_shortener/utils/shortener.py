from aiogram.dispatcher import FSMContext

from client import VKClient, BITClient

CLIENTS = {
    str(VKClient): VKClient,
    str(BITClient): BITClient
}


async def get_client(state: FSMContext):
    state_data = await state.get_data()

    return CLIENTS[state_data.get('shortener', 'VK')]
