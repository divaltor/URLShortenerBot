from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import FSMContext
from aiogram import types


class ClientMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, msg: types.Message, data: dict):

        state: FSMContext = data.get('state')

        state_data = await state.get_data()

        if state_data.get('shortener') is None:
            await state.update_data(shortener='vk.cc')
