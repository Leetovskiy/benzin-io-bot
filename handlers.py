"""User message handlers"""
import re

from aiogram import types
from aiogram.types import ContentType

from loader import dp
from utils import send_result_by_url, is_image

URL_REGEXP_PATTERN = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'(\)\*\+\%=.]+$'


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        'Привет! Я бот, который может убрать фон с твоего фото.\n'
        'Просто отправь мне любое изображение, ссылку на него или документ')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer(
        'Чтобы удалить фон отправь мне любое изображение, ссылку на него или '
        'документ\n\n'
        'Команды:\n'
        '/start – запуск бота\n'
        '/help – посмотреть подсказку')


@dp.message_handler(content_types=(ContentType.PHOTO, ContentType.DOCUMENT))
async def photo_handler(message: types.Message):
    if message.content_type is ContentType.PHOTO:
        input_object = message.photo[-1]
    else:
        input_object = message.document
        if not await is_image(input_object):
            await message.reply(
                '*Ошибка*\nДокумент должен быть изображением\!',
                parse_mode='MarkdownV2')
            return

    url = await input_object.get_url()
    await send_result_by_url(message, url)


@dp.message_handler(regexp=URL_REGEXP_PATTERN)
async def url_handler(message: types.Message):
    url = re.match(URL_REGEXP_PATTERN, message.text).group(0)
    await send_result_by_url(message, url)


@dp.message_handler(lambda _: True)
async def any_message_handler(message: types.Message):
    await message.reply('Я принимаю только команды или изображения\n'
                        'Подсказка: /help')
