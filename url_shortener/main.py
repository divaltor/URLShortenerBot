from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from loguru import logger

import config

import handlers
import middlewares
import filters

storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASS)
bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

# Add logger
logger.add('../info.log', rotation='1 week')


async def on_startup(dp: Dispatcher):
    filters.setup(dp)
    handlers.setup(dp)
    middlewares.setup(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
