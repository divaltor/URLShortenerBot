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

if __name__ == '__main__':
    executor.start_polling(dp)
