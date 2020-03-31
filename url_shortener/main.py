from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

import config
from middlewares.client_middleware import ClientMiddleware
from middlewares.i18n import i18n

import handlers.inlines as inlines
import handlers.messages as messages
import handlers.callbacks as callbacks

storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT)
bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

# Setup middleware
dp.middleware.setup(ClientMiddleware())
dp.middleware.setup(i18n)
dp.middleware.setup(LoggingMiddleware())

# Add logger
logger.add('../info.log', rotation='1 week')

# Setup dispatcher
dp.register_message_handler(types.ChatType.is_private, messages.send_start, commands='start')
dp.register_message_handler(types.ChatType.is_private, messages.handle_settings, text='⚙Settings')
dp.register_message_handler(types.ChatType.is_private, messages.handle_language, text='🇺🇸Language')
dp.register_message_handler(types.ChatType.is_private, messages.handle_link, regexp=r'^(https?:\/\/[^\s]+)$')

dp.register_callback_query_handler(types.ChatType.is_private, callbacks.change_language, lambda call: call.data.startswith('lang'))
dp.register_callback_query_handler(types.ChatType.is_private, callbacks.change_client, lambda call: call.data.startswith('client'))

dp.register_inline_handler(inlines.handle_inline_link, regexp=r'^(https?:\/\/[^\s]+)$')


if __name__ == '__main__':
    executor.start_polling(dp)
