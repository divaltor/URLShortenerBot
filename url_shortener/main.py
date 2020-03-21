from aiogram import Bot, Dispatcher, executor, types
from loguru import logger

import os

import client

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

    response = await client.VKClient.get('/method/utils.getShortLink', params={'url': url})
    response = response.json()

    if response.get('response') is not None:
        return await msg.reply(f'Short link: {response["response"]["short_url"]}', disable_web_page_preview=True)

    await msg.reply(f'<b>Invalid link</b>')
    logger.error(f'Error message of response: {response["error"]["error_msg"]}. Error code: {response["error"]["error_code"]}')


@dp.inline_handler(regexp=r'^(https?:\/\/[^\s]+)$')
async def handle_inline_link(inline_query: types.InlineQuery):
    text = inline_query.query
    response = (await client.VKClient.get('/method/utils.getShortLink', params={'url': text})).json()

    if response.get('response'):
        input_content = types.InputTextMessageContent(response['response']['short_url'])
    else:
        input_content = types.InputTextMessageContent('Invalid link')
    result_id = hashlib.md5(text.encode()).hexdigest()
    item = types.InlineQueryResultArticle(
        id=result_id,
        title=f'Short link: {response["response"]["short_url"]}',
        input_message_content=input_content
    )

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp)
