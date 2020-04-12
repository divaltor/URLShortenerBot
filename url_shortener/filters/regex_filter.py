import re

from aiogram import types
from aiogram.dispatcher.filters.filters import BoundFilter

WRONG_CHARS = {
    ord(' '): '%20'
}

LINK_PATTERN = re.compile(r'((?:http|https)://(?:\w+:?\w*@)?(?:\S+)(?::[0-9]+)?(?:/|/(?:[\w#!:.?+=&%@\-/]))?)')


class RegexFilter(BoundFilter):
    key = 'regex'

    def __init__(self, regex):
        self.regex = regex

    async def check(self, message: types.Message) -> bool:
        if re.search(LINK_PATTERN, message.text.translate(WRONG_CHARS)):
            return True
