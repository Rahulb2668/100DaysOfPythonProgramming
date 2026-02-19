import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
url = "https://pro.openweathermap.org/data/2.5/forecast"
twilio_account_id = os.environ.get("TWILIO_ACCOUNT_ID")
twilio_account_auth = os.environ.get("TWILIO_ACCOUNT_AUTH")


weather_api_params = {
    "lat":9.074238866415161,
    "lon":126.19900476739134,
    "appid":api_key,
    "cnt":4
}
response = requests.get(url,params=weather_api_params )
response.raise_for_status()

weather_data = response.json()

condition_code = [hr_data["weather"][0]["id"] for hr_data in weather_data["list"]]

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_account_id, twilio_account_auth)
    message = client.messages.create(
        body="Please take umbrella. Its going to rain",
        from_="+18065831924",
        to="+18777804236",
    )
    print(message.status)
