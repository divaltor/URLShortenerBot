from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import FSMContext
from loguru import logger

import hashlib

import config
from middlewares.client_middleware import ClientMiddleware

from utils.shortener import get_client, CLIENTS

storage = RedisStorage2(password=config.REDIS_PASS)
bot = Bot(config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(ClientMiddleware())

logger.add('../info.log', rotation='1 week')


@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message, state: FSMContext):

    logger.debug(f'{state=}')

    setting_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    setting_keyboard.add(types.KeyboardButton('⚙️ Settings'))

    await msg.answer('Send link like https://example.com', reply_markup=setting_keyboard)


@dp.message_handler(lambda msg: msg.text == '⚙️ Settings')
async def handle_settings(msg: types.Message, state: FSMContext):
    shortener = await get_client(state)

    shorteners = [name for name in CLIENTS.keys()]

    shorteners_keyboard = types.InlineKeyboardMarkup(row_width=3)
    shorteners_keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=f'client,{name}') for name in shorteners])

    await msg.answer(f'Current shortener is: <b>{shortener}</b>\n\n'
                     f'Available shorteners: <b>{", ".join([name for name in shorteners])}</b>',
                     reply_markup=shorteners_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith('client'))
async def change_client(query: types.CallbackQuery, state: FSMContext):
    data = query.data.split(',')[1]

    await state.update_data(shortener=data)

    current_shortener = (await state.get_data()).get('shortener')

    await bot.edit_message_text(f'Current shortener is: <b>{current_shortener}</b>', query.from_user.id, query.message.message_id)

    await bot.answer_callback_query(query.id)


@dp.message_handler(regexp=r'^(https?:\/\/[^\s]+)$')
async def handle_link(msg: types.Message, state: FSMContext):
    url = msg.text
    client = await get_client(state)

    short_url = await client.get_short_link(url)

    if response.get('response') is not None:
        return await msg.reply(f'Short link: {response["response"]["short_url"]}', disable_web_page_preview=True)

    await msg.reply(f'<b>Invalid link</b>')


@dp.inline_handler(regexp=r'^(https?:\/\/[^\s]+)$')
async def handle_inline_link(inline_query: types.InlineQuery, state: FSMContext):
    text = inline_query.query
    client = await get_client(state)

    short_url = await client.get_short_link(text)

    if short_url is not None:
        input_content = types.InputTextMessageContent(short_url)
        title = f'Short link: {short_url}'
        result_id = hashlib.md5(text.encode()).hexdigest()
        item = types.InlineQueryResultArticle(
            id=result_id,
            title=title,
            input_message_content=input_content
        )

        return await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)

    return


if __name__ == '__main__':
    executor.start_polling(dp)
