'''
Based on https://github.com/slackapi/python-slackclient/tree/master/tutorial/PythOnBoardingBot
'''

import certifi
import logging
import pathlib
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
from adjutant import Adjutant
# from onboarding_tutorial import OnboardingTutorial


class MockLoad:
    def load(*args):
        return {'SLACK_SIGNING_SECRET': 'SECRET',
                'SLACK_BOT_TOKEN': 'TOKEN'}


adjutant = Adjutant(pathlib.Path.cwd().joinpath('adjutant'), MockLoad())

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    adjutant.memory['SLACK_SIGNING_SECRET'],
    endpoint="/slack/events",
    server=app)

# Initialize a Web API client
slack_web_client = WebClient(token=adjutant.memory['SLACK_BOT_TOKEN'])

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_events_adapter.on("message")
def message(payload):
    """General handling of messages received."""
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id    = event.get("user")
    text       = event.get("text")

    if text and text.lower().startswith('adjutant') and \
            text.lower().endswith('please'):
        response = adjutant.parse_order(text)
        print(response)
        slack_web_client.chat_postMessage(channel=channel_id, text=response)

    elif text and text.lower().startswith('adjutant') and \
            not text.lower().endswith('please'):
        slack_web_client.chat_postMessage(channel=channel_id,
                                          text="You didn't say the magic word")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    app.run(port=3000)
