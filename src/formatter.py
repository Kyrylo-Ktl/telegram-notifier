# -*- coding: utf-8 -*-
"""Module with telegram log messages formatter."""

from logging import Formatter, LogRecord
from time import strftime


class TelegramLogMessageFormatter(Formatter):
    """Formatter for telegram log messages."""

    def format(self, record: LogRecord) -> str:
        return '<b>{datetime}</b>\n{message}'.format(
            datetime=strftime('%Y-%m-%d %H:%M:%S'),
            message=record.msg,
        )
