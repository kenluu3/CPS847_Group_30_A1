from dotenv import load_dotenv
from flask import Flask, request, Response
import os
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from pathlib import Path
import requests

# .env file from root
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# api tokens
token = os.getenv("BOT_TOKEN")
sign_in_sec = os.getenv("SIGN_IN_SECRET")
weather_key=os.getenv("API_KEY")

# Creating flask app.
app = Flask(__name__)

# events
slack_events_adapter = SlackEventAdapter(sign_in_sec, "/bot/events", app)

# Slack Bot Info
client = WebClient(token=token)
BOT_ID = client.auth_test().get("user_id")

# slash commands
@app.route('/weather', methods=['GET','POST'])
def getWeather():
    city = request.form.get('text')
    if(not city):
        client.chat_postMessage(
            channel="#assignment1",
            text="City Argument Missing [city]"
        )
        return Response(), 400
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+weather_key+"&units=metric"
    response = requests.get(url).json()

    if(response.get("cod") == "404"):
        client.chat_postMessage(
            channel="#assignment1",
            text="City not found"
        )
        return Response(), 404

    message="The temperature for " + city + " is " + str(response.get("main").get("temp")) + " degrees Celsius with " + str(response.get("weather")[0].get("description")) + "."
    client.chat_postMessage(
        channel="#assignment1",
        text=message
    )
    return Response(), 200

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
