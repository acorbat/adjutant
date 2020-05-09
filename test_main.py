from start_bot import message, slack_web_client
import pytest


def test_message():
    payload = {'event': {}}
    assert message(payload) is None


def test_message_does_nothing(mock_chat_postMessage):
    payload = {'event': {'text': 'in a bottle'}}
    message(payload)
    slack_calls = slack_web_client.chat_postMessage.calls
    assert len(slack_calls) == 0


def test_unpolite_message_adjutant(mock_chat_postMessage):
    payload = {'event': {'text': 'adjutant in a bottle'}}
    message(payload)
    response = {'channel': None, 'text': "You didn't say the magic word"}
    slack_calls = slack_web_client.chat_postMessage.calls
    assert len(slack_calls) == 1
    assert response == slack_calls[0]


def test_polite_message_adjutant(mock_chat_postMessage):
    payload = {'event': {'text': 'adjutant in a bottle'}}
    message(payload)
    response = {'channel': None, 'text': "You didn't say the magic word"}
    slack_calls = slack_web_client.chat_postMessage.calls
    assert len(slack_calls) == 1
    assert response == slack_calls[0]


class messengerSpy:

    def __init__(self):
        self._calls = []

    def __call__(self, **kwargs):
        self.calls = kwargs

    @property
    def calls(self):
        return self._calls

    @calls.setter
    def calls(self, value):
        self._calls.append(value)


@pytest.fixture
def mock_chat_postMessage(monkeypatch):
    monkeypatch.setattr(slack_web_client, "chat_postMessage", messengerSpy())


def test_message(mock_chat_postMessage):
    # with mock.patch('start_bot.slack_web_client') as swc:
    payload = {'event': {'text': 'adjutant in a bottle'}}
    message(payload)
    response = {'channel': None, 'text': "You didn't say the magic word"}
    calls = slack_web_client.chat_postMessage.calls
    assert response == calls[0]
    assert len(calls) == 1