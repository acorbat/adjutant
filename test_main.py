from start_bot import message
from unittest import mock


def test_message():
    with mock.patch('start_bot.Adjutant'):
        payload = {'event': {}}
        message(payload)
