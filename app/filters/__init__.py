from aiogram import Dispatcher

from .regex_filter import RegexFilter
from .inline_filter import InlineFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(RegexFilter, event_handlers=[dp.message_handlers, dp.inline_query_handlers])
    dp.filters_factory.bind(InlineFilter, event_handlers=[dp.inline_query_handlers])
