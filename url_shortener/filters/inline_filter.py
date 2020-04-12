from aiogram import types
from aiogram.dispatcher.filters.filters import BoundFilter

from filters.regex_filter import WRONG_CHARS


class InlineFilter(BoundFilter):
    key = 'len_restrict'

    def __init__(self, len_restrict):
        self.len_restrict = len_restrict

    async def check(self, inline_query: types.InlineQuery) -> bool:
        if len(inline_query.query.translate(WRONG_CHARS)) < 256:
            return True
