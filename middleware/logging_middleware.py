from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from loguru import logger


class LoggingMiddleware(BaseMiddleware):

    @classmethod
    async def on_process_message(cls, message: Message, data: dict):
        username, user_id = message.from_user.username, data['state'].user
        logger.info(f'Message from @{username} (id: {user_id}): {message}')
