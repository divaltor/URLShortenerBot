from aiogram import types

from middlewares.i18n import _


def get_lang_keyboard():
    setting_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    setting_keyboard.add(*[
        types.KeyboardButton(_('⚙Settings')),
        types.KeyboardButton(_('🇺🇸Language'))
    ])

    return setting_keyboard
