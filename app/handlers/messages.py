from aiogram import types
from aiogram.dispatcher import FSMContext

from app.utils.shortener import get_lang, get_client, CLIENTS, translate_chars
from app.middlewares.i18n import _, i18n


async def send_start(msg: types.Message):
    setting_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    setting_keyboard.add(*[
        types.KeyboardButton('⚙Settings'),
        types.KeyboardButton('🇺🇸Language')
    ])

    await msg.answer(_('Send link like {link}').format(link='https://example.com'), reply_markup=setting_keyboard)


async def handle_settings(msg: types.Message, state: FSMContext):
    shortener = await get_client(state)

    shorteners = [name for name in CLIENTS.keys()]

    shorteners_keyboard = types.InlineKeyboardMarkup()
    shorteners_keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=f'client,{name}') for name in shorteners])

    await msg.answer(_('Current shortener is: <b>{shortener}</b>\n\n'
                       'Available shorteners: <b>{shorteners}</b>').format(
        shortener=shortener,
        shorteners=", ".join([name for name in shorteners])
    ),
        reply_markup=shorteners_keyboard)


async def handle_language(msg: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text=f'{lang.flag} {lang.title}',
            callback_data=f'lang,{lang_name}'
        )
        for lang_name, lang in i18n.AVAILABLE_LANGUAGES.items()
    ])

    language = await get_lang(state)

    await msg.answer(_('Current language: {language}').format(language=language), reply_markup=keyboard)


async def handle_link(msg: types.Message, state: FSMContext):
    url = translate_chars(msg.text)
    client = await get_client(state)

    short_url = await client.get_short_link(url)

    if short_url is not None:
        return await msg.reply(_('Short link: {short_url}').format(short_url=short_url), disable_web_page_preview=True)

    await msg.reply(_(f'<b>Invalid link</b>'))

__all__ = ['handle_link', 'handle_language', 'handle_settings']