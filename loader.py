"""Loads some objects for use in future"""

import logging
import os

from aiogram import Bot, Dispatcher

from benzin.api import Benzin

BOT_TOKEN = os.getenv('BOT_TOKEN')
BENZIN_TOKEN = os.getenv('BENZIN_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
benzin = Benzin(BENZIN_TOKEN)
