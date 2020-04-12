import hashlib

from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.shortener import get_client
from middlewares.i18n import _
from filters.regex_filter import WRONG_CHARS


async def handle_inline_link(inline_query: types.InlineQuery, state: FSMContext):
    text = inline_query.query.translate(WRONG_CHARS)
    client = await get_client(state)

    short_url = await client.get_short_link(text)

    if short_url is not None:
        input_content = types.InputTextMessageContent(short_url)
        title = _('Short link: {short_url}').format(short_url=short_url)
        result_id = hashlib.md5(text.encode()).hexdigest()
        item = types.InlineQueryResultArticle(
            id=result_id,
            title=title,
            input_message_content=input_content
        )

        return await inline_query.answer(results=[item], cache_time=3)

    return

__all__ = ['handle_inline_link']
