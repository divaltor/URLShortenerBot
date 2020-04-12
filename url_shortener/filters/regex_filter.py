import re
from typing import Union

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

    async def check(self, message: Union[types.Message, types.InlineQuery]) -> bool:
        text = message.text if isinstance(message, types.Message) else message.query
        if re.search(LINK_PATTERN, text.translate(WRONG_CHARS)):
            return True
