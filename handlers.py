"""User message handlers"""

from tempfile import NamedTemporaryFile

from aiogram import types
from requests.exceptions import RequestException

from loader import benzin
from loader import dp


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer('Привет! Я бот, который может убрать фон с твоего фото.\n'
                         'Просто отправь мне любую фотографию')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer('Чтобы удалить фон с фото просто отправь мне его\n\n'
                         'Команды:\n'
                         '/start – запуск бота\n'
                         '/help – посмотреть подсказку')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    status_message = await message.reply('Обрабатываю…', disable_notification=True)
    url = await message.photo[-1].get_url()

    try:

        response = benzin.upload_by_url(url, size='full')
    except RequestException:
        await message.reply('Ошибка при обработке запроса ;('
                            'Попробуйте позже или обратитесь к разработчику')
        return

    with NamedTemporaryFile('wb', prefix='clear_', suffix='.png') as file:
        file.write(response.content)
        image_file = types.InputFile(file.name)
        await message.reply_document(image_file)
    await status_message.delete()


@dp.message_handler(lambda _: True)
async def any_message_handler(message: types.Message):
    await message.reply('Неизвестная команда!\n'
                        'Подсказка: /help')
