import smtplib
import time

import requests
import datetime


MY_LAT = 25.204849
MY_LNG= 55.270782

MY_EMAIL = ""
MY_PASSWORD = ""

def is_iss_overhead():
    ## ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    pos_data = response.json()["iss_position"]

    iss_latitude = float(pos_data["latitude"])
    iss_longitude = float(pos_data["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5


def is_night():
    parameters  = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }

    res = requests.get(url = "https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()

    data = res.json()["results"]

    sunrise_time = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(data["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.datetime.now().hour

    return time_now > sunset_time or time_now < sunrise_time

def send_email():
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"LOOK UP")
    except Exception as e:
        print(e)

while True:
    if is_iss_overhead() and is_night():
        send_email()
    time.sleep(60)