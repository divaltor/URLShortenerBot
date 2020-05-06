from . import i18n
from . import client_middleware

from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(i18n.i18n)
    dp.middleware.setup(client_middleware.ClientMiddleware())
    dp.middleware.setup(LoggingMiddleware())