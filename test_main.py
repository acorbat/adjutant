from start_bot import message
from unittest import mock


def test_message():
    payload = {'event': {}}
    assert message(payload) is None


def test_no_message_does_nothing():
    with mock.patch('start_bot.slack_web_client') as swc:
        payload = {'event': {}}
        message(payload)
        assert 'chat_postMessage' not in dir(swc)


def test_message_does_nothing():
    with mock.patch('start_bot.slack_web_client') as swc:
        payload = {'event': {'text': 'in a bottle'}}
        message(payload)
        assert 'chat_postMessage' not in dir(swc)


def test_unpolite_message_adjutant():
    with mock.patch('start_bot.slack_web_client') as swc:
        payload = {'event': {'text': 'adjutant in a bottle'}}
        message(payload)
        response = {'channel': None, 'text': "You didn't say the magic word"}
        swc.chat_postMessage.assert_called_with(**response)


def test_polite_message_adjutant():
    with mock.patch('start_bot.slack_web_client') as swc:
        payload = {'event': {'text': 'adjutant in a bottle please'}}
        message(payload)
        response = {'channel': None, 'text': 'I could not understand your order'}
        swc.chat_postMessage.assert_called_with(**response)