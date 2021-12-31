"""Handy functions"""

import imghdr
from base64 import b64decode
from tempfile import NamedTemporaryFile

from aiogram import types
from aiogram.types import Document
from loguru import logger

from benzin.exceptions import ResponseError
from loader import benzin


async def is_image(document: Document) -> bool:
    """Check if Telegram document is image

    Args:
        document: Instance of aiogram.types.Document

    Raises:
        TypeError: If the type of the passed document is wrong

    Return:
        True or False
    """
    if not isinstance(document, Document):
        raise TypeError

    with NamedTemporaryFile('wb') as file:
        await document.download(destination_file=file.name)
        return bool(imghdr.what(file.name))


@logger.catch
async def send_result_by_url(message: types.Message, image_url: str):
    """Removes background from image by URL and send result to user"""
    status_message = await message.reply('Обрабатываю…', disable_notification=True)
    try:
        response = await benzin.remove_background(
            image_file_url=image_url,
            size='full',
            output_format='json',
        )

        with NamedTemporaryFile('wb', prefix='@ClearBG_bot-', suffix='.png') as file:
            decoded_image = b64decode(response['image_raw'])
            file.write(decoded_image)
            image_file = types.InputFile(file.name)
            await message.reply_document(image_file)
    except ResponseError:
        logger.exception(f'Benzin API response error occurred from message: {message}')
        await message.reply(f'*Ошибка при обработке запроса:*\n'
                            f'Отправьте другое изображение/ссылку, попробуйте '
                            f'позже или обратитесь к разработчику',
                            parse_mode='MarkdownV2')
        return
    finally:
        await status_message.delete()
