import requests
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "DUMMY"
TWILIO_AUTH_TOKEN = "DUMMY"

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
MY_LAT = 1.3521
MY_LONG = 103.8198
API_KEY = "dbaa6e781305279af45afe5e48783eec"

# https://api.openweathermap.org/data/2.8/onecall?lat=1.3521&lon=103.8198&exclude=current,minutely,daily,alerts&units=metric&appid=dbaa6e781305279af45afe5e48783eec

response = requests.get(f"{WEATHER_ENDPOINT}?lat={MY_LAT}&lon={MY_LONG}&exclude=current,minutely,daily,alerts&units=metric&appid={API_KEY}")
response.raise_for_status()
data = response.json()

#JSON Viewer: http://jsonviewer.stack.hu/#https://api.openweathermap.org/data/2.5/onecall?lat=1.3521&lon=103.8198&exclude=current,minutely,daily,alerts&units=metric&appid=dbaa6e781305279af45afe5e48783eec
#Slice documentation: https://stackoverflow.com/questions/509211/understanding-slicing
#Weather condition codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

will_rain = False

###TODO: Retrieve weather condition for next 12h
weather_slice = data["hourly"][:12]
for hour in weather_slice:
    condition = hour["weather"][0]["id"]
    if condition <600:
        will_rain = True

if will_rain:
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "☂️Today you'll be needing your umbrella-ella☂️",
        from_ = "+12345678910",
        to = "+6512345678"
    )

    print(message.sid)
