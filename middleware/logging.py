# Copyright © 2022 Vitaliy Zaitsev. All rights reserved.
# Contacts: dev.zaitsev@gmail.com
# Licensed under the Apache License, Version 2.0
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from loguru import logger


class LoggingMiddleware(BaseMiddleware):

    @classmethod
    async def on_process_message(cls, message: Message, data: dict):
        log_string = f'(chat: {message.chat.id}; message: {message.message_id})'
        logger.info(f'Message received {log_string}')
