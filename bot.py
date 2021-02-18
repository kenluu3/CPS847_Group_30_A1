from dotenv import load_dotenv
from flask import Flask
import os
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from pathlib import Path

# .env file from root
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# api tokens
token = os.getenv("BOT_TOKEN")
sign_in_sec = os.getenv("SIGN_IN_SECRET")

# Creating flask app.
app = Flask(__name__)

# events
slack_events_adapter = SlackEventAdapter(sign_in_sec, "/bot/events", app)

# Slack Bot Info
client = WebClient(token=token)
BOT_ID = client.auth_test().get("user_id")

# bot event listeners
@slack_events_adapter.on("message")
def message(payload): # echos the message back.
    if payload == {}:
        return
    else:
        data = payload.get("event")
        if (data.get("user") != BOT_ID):
            client.chat_postMessage(
                channel="#assignment1",
                text=data.get("text")
            )

# start app
if __name__ == "__main__":
    app.run(debug=True)
