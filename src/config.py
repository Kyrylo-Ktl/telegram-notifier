# -*- coding: utf-8 -*-
"""Configuration module."""

import logging
import os
from logging import StreamHandler

from dotenv import load_dotenv

from .formatter import TelegramLogMessageFormatter as Formatter
from .handler import TelegramNotificationsHandler as Handler

load_dotenv()

TOKEN_ID = os.getenv('TOKEN_ID')
CHAT_IDS = os.getenv('CHAT_IDS').split(',')

LOG_CONFIG = {
    'version': 1,
    'loggers': {
        'root': {
            'handlers': ['console', 'telegram'],
            'level': logging.DEBUG,
        },
    },
    'handlers': {
        'console': {
            'class': f'{StreamHandler.__module__}.{StreamHandler.__qualname__}',
            'formatter': 'console_formatter',
            'level': logging.DEBUG,
        },
        'telegram': {
            'class': f'{Handler.__module__}.{Handler.__qualname__}',
            'token_id': TOKEN_ID,
            'chat_ids': CHAT_IDS,
            'formatter': 'telegram_formatter',
            'level': logging.WARNING,
        },
    },
    'formatters': {
        'console_formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'telegram_formatter': {
            'class': f'{Formatter.__module__}.{Formatter.__qualname__}',
        },
    },
}
