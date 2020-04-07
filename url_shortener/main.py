from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

import config
from middlewares.client_middleware import ClientMiddleware
from middlewares.i18n import i18n

import handlers

storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT)
bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

# Setup middleware
dp.middleware.setup(ClientMiddleware())
dp.middleware.setup(i18n)
dp.middleware.setup(LoggingMiddleware())

# Add logger
logger.add('../info.log', rotation='1 week')


async def on_startup(dp: Dispatcher):
    handlers.setup(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
