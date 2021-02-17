from dotenv import load_dotenv
from flask import Flask
import os
import slack
from pathlib import Path

# .env file from root
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# api token
token = os.getenv("BOT_TOKEN")

# Creating flask app.
app = Flask(__name__)

print(token)
# bot client
bot = slack.WebClient(token=token)

#random msg.
bot.chat_postMessage(channel='#general', text="Hello World")

@app.route("/")
def root():
    return "Hello World"

@app.route("/test")
def smthn():
    return "Something else"

# load Slack token
token = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    app.run(debug=True)
