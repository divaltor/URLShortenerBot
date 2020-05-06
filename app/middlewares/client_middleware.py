from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import FSMContext


class ClientMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, msg: types.Message, data: dict):
        state: FSMContext = data.get('state')

        async with state.proxy() as state_data:
            if state_data.get('shortener') is None:
                state_data['shortener'] = 'clck.ru'

            if state_data.get('locale') is None:
                state_data['locale'] = 'en'
