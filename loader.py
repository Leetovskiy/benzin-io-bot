"""Loads some objects for use in future"""

import logging
import os
import sys

from aiogram import Bot, Dispatcher
from loguru import logger

from benzin.api import Benzin
from middleware.logging_middleware import LoggingMiddleware

# Disable default aiogram logging
logging.getLogger('aiogram').disabled = True

# Logging configuration
STDOUT_LOG_FORMAT = '<green>{time}</green> | <level>{level}</level>\t <level>{message}</level>'
logger.remove()
logger.add(sys.stdout, format=STDOUT_LOG_FORMAT, level=0, colorize=True, backtrace=False, enqueue=True)

# Load secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
BENZIN_TOKEN = os.getenv('BENZIN_TOKEN')

# Objects instantiation
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
benzin = Benzin(BENZIN_TOKEN)

# Enable aiogram middleware
dp.middleware.setup(LoggingMiddleware())
