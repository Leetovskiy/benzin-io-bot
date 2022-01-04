from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from loguru import logger


class LoggingMiddleware(BaseMiddleware):

    @classmethod
    async def on_process_message(cls, message: Message, data: dict):
        logger.info(f'Message received: {message}')
