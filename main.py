# Copyright © 2022 Vitaliy Zaitsev. All rights reserved.
# Contacts: dev.zaitsev@gmail.com
# Licensed under the Apache License, Version 2.0
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
