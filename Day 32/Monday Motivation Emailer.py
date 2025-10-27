import random
import smtplib
import datetime as dt


MY_EMAIL = ""
PASSWORD=""

def send_email():
    try:
        with open("quotes.txt") as quotesFile:
            lines = quotesFile.readlines()
            quote = random.choice(lines)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Monday\n\n{quote}")
    except Exception as e:
        print(e)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    send_email()

