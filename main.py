"""Main script"""

from aiogram import executor
from loguru import logger

import handlers
from loader import dp

if __name__ == '__main__':
    try:
        logger.info('Bot start')
        executor.start_polling(dispatcher=dp, skip_updates=True)
    finally:
        logger.info('Bot stopped')
