import hashlib

from aiogram import types
from aiogram.dispatcher import FSMContext

from app.utils.shortener import get_client, translate_chars
from app.middlewares.i18n import _


async def handle_inline_link(inline_query: types.InlineQuery, state: FSMContext):
    text = translate_chars(inline_query.query)

    result_id = hashlib.md5(text.encode()).hexdigest()
    client = await get_client(state)

    short_url = await client.get_short_link(text)

    if short_url is not None:
        input_content = types.InputTextMessageContent(short_url)
        title = _('Short link: {short_url}').format(short_url=short_url)
        item = types.InlineQueryResultArticle(
            id=result_id,
            title=title,
            input_message_content=input_content
        )

        return await inline_query.answer(results=[item], cache_time=3)

    return


async def handle_wrong_inline_link(inline_query: types.InlineQuery):
    result_id = hashlib.md5(inline_query.query.encode()).hexdigest()

    input_content = types.InputTextMessageContent('Link greater than 256 characters')
    title = _('Link greater than 256 characters')
    item = types.InlineQueryResultArticle(
        id=result_id,
        title=title,
        input_message_content=input_content
    )

    return await inline_query.answer(results=[item], cache_time=300)

__all__ = ['handle_inline_link']
