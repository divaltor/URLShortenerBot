from . import messages
from . import callbacks
from . import inlines

from aiogram.dispatcher import Dispatcher
from aiogram import types


def setup(dp: Dispatcher):
    dp.register_message_handler(messages.send_start, types.ChatType.is_private, commands='start')
    dp.register_message_handler(messages.handle_settings, types.ChatType.is_private, text='⚙Settings')
    dp.register_message_handler(messages.handle_language, types.ChatType.is_private, text='🇺🇸Language')
    dp.register_message_handler(messages.handle_link, types.ChatType.is_private, regex=True)

    dp.register_callback_query_handler(callbacks.change_language, lambda call: call.data.startswith('lang'))
    dp.register_callback_query_handler(callbacks.change_client, lambda call: call.data.startswith('client'))

    dp.register_inline_handler(inlines.handle_inline_link, regex=True, len_restrict=True)
    dp.register_inline_handler(inlines.handle_wrong_inline_link, regex=True)
