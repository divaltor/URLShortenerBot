from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.shortener import get_lang
from middlewares.i18n import _


async def change_language(query: types.CallbackQuery, state: FSMContext):
    data = query.data.split(',')[1]

    async with state.proxy() as state_data:
        state_data['locale'] = data

    language = await get_lang(state)

    await query.message.edit_text(_('Current language: {language}', locale=data).format(language=language))

    await query.answer()


async def change_client(query: types.CallbackQuery, state: FSMContext):
    data = query.data.split(',')[1]

    async with state.proxy() as state_data:
        state_data['shortener'] = data

    current_shortener = (await state.get_data()).get('shortener')

    await query.message.edit_text(_('Current shortener is: <b>{current_shortener}</b>').format(current_shortener=current_shortener))

    await query.answer()

__all__ = ['change_language', 'change_client']
