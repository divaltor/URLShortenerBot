from aiogram import types
from aiogram.dispatcher.filters.filters import BoundFilter

from utils.shortener import translate_chars


class InlineFilter(BoundFilter):
    key = 'len_restrict'

    def __init__(self, len_restrict):
        self.len_restrict = len_restrict

    async def check(self, inline_query: types.InlineQuery) -> bool:
        if len(translate_chars(inline_query.query)) < 256:
            return True

        return False
