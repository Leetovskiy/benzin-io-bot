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
STDOUT_LOG_FORMAT = '<green>{time}</green> | <level>{level: <8}</level>\t <level>{message}</level>'
logger.remove()
logger.add(sys.stdout, format=STDOUT_LOG_FORMAT, level=0, colorize=True, backtrace=False, enqueue=True)

IS_LOGFILE = os.getenv('IS_LOGFILE')
if IS_LOGFILE == 'TRUE':
    logger.add('journal.log', rotation='500 MB', compression='zip')
else:
    logger.warning('Logging to a file is disabled')

# Load secrets
BOT_TOKEN = os.getenv('BOT_TOKEN')
BENZIN_TOKEN = os.getenv('BENZIN_TOKEN')

# Objects instantiation
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
benzin = Benzin(BENZIN_TOKEN)

# Enable aiogram middleware
dp.middleware.setup(LoggingMiddleware())
