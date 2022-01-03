"""Main script"""

from aiogram import executor
from loguru import logger

# noinspection PyUnresolvedReferences
import handlers
from loader import dp

if __name__ == '__main__':
    try:
        logger.info('Bot has started')
        executor.start_polling(dispatcher=dp, skip_updates=True)
    finally:
        logger.info('Bot has stopped')
