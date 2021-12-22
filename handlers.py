"""User message handlers"""
import re
from base64 import b64decode
from tempfile import NamedTemporaryFile

from aiogram import types
from aiohttp.client_exceptions import ClientResponseError

from loader import benzin
from loader import dp

URL_REGEXP_PATTERN = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'(\)\*\+\%=.]+$'


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer('Привет! Я бот, который может убрать фон с твоего '
                         'фото.\n Просто отправь мне любую фотографию или '
                         'ссылку на него')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer('Чтобы удалить фон отправь мне изображение или его '
                         'ссылку, по которой он доступен в сети.\n\n'
                         'Команды:\n'
                         '/start – запуск бота\n'
                         '/help – посмотреть подсказку')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    url = await message.photo[-1].get_url()
    await send_result_by_url(message, url)


@dp.message_handler(regexp=URL_REGEXP_PATTERN)
async def url_handler(message: types.Message):
    url = re.match(URL_REGEXP_PATTERN, message.text).group(0)
    await send_result_by_url(message, url)


@dp.message_handler(lambda _: True)
async def any_message_handler(message: types.Message):
    await message.reply('Неизвестная команда!\n'
                        'Подсказка: /help')


async def send_result_by_url(message: types.Message, image_url: str):
    """Removes background from image by URL and send result to user"""
    status_message = await message.reply('Обрабатываю…', disable_notification=True)
    try:
        response = await benzin.remove_background_by_url(image_url, size='full')

        with NamedTemporaryFile('wb', prefix='clear_', suffix='.png') as file:
            decoded_image = b64decode(response['image_raw'])
            file.write(decoded_image)
            image_file = types.InputFile(file.name)
            await message.reply_document(image_file)
    except ClientResponseError:
        await message.reply('*Ошибка при обработке запроса ;\(*\n\n'
                            'Отправьте другое изображение/ссылку, попробуйте '
                            'позже или обратитесь к разработчику',
                            parse_mode='MarkdownV2')
        return
    except Exception:
        await message.reply('*Неожиданная ошибка ;\(*\n\nОтправьте другое '
                            'изображение/ссылку, попробуйте позже или '
                            'обратитесь к разработчику',
                            parse_mode='MarkdownV2')
        return
    finally:
        await status_message.delete()
