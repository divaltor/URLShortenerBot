from aiogram import Bot, Dispatcher, executor, types
from loguru import logger

import os

from client import VKClient, BITClient

import config

bot = Bot(config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

logger.add('../info.log', rotation='1 week')


@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    await msg.reply('Отправьте ссылку формата: https://example.com')


@dp.message_handler(regexp=r'^(https?:\/\/[^\s]+)$')
async def handle_link(msg: types.Message):
    url = msg.text

    short_url = await VKClient.get_short_link(url)

    if response.get('response') is not None:
        return await msg.reply(f'Short link: {response["response"]["short_url"]}', disable_web_page_preview=True)

    await msg.reply(f'<b>Invalid link</b>')


@dp.inline_handler(regexp=r'^(https?:\/\/[^\s]+)$')
async def handle_inline_link(inline_query: types.InlineQuery):
    text = inline_query.query
    short_url = await VKClient.get_short_link(text)

    if short_url is not None:
        input_content = types.InputTextMessageContent(short_url)
        title = f'Short link: {short_url}'
        result_id = hashlib.md5(text.encode()).hexdigest()
        item = types.InlineQueryResultArticle(
            id=result_id,
            title=title,
            input_message_content=input_content
        )

        await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)

    return

if __name__ == '__main__':
    executor.start_polling(dp)
