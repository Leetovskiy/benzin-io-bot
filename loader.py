"""Loads some objects for use in future"""

import logging
import os

from aiogram import Bot, Dispatcher
from loguru import logger

from benzin.api import Benzin


class InterceptHandler(logging.Handler):
    """Intercepting existing logs and transfer to loguru"""

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=0)
logger.add('journal.log', compression='zip', rotation='500 MB')

BOT_TOKEN = os.getenv('BOT_TOKEN')
BENZIN_TOKEN = os.getenv('BENZIN_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
benzin = Benzin(BENZIN_TOKEN)
