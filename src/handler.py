# -*- coding: utf-8 -*-
"""Module with telegram notifications handler."""

from logging import Handler, LogRecord

import requests


class TelegramNotificationsHandler(Handler):
    """Handler for sending log messages to specified telegram chats.

    Args:
        token_id (str): Telegram bot token.
        chat_ids (list): List of chat IDs where the log message will be sent.
    """

    def __init__(self, token_id: str, chat_ids: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__token_id = token_id
        self.__chat_ids = chat_ids

    def emit(self, record: LogRecord):
        for chat_id in self.__chat_ids:
            requests.post(
                url=f'https://api.telegram.org/bot{self.__token_id}/sendMessage',
                data={
                    'chat_id': chat_id,
                    'text': self.format(record),
                    'parse_mode': 'HTML',
                },
            )
