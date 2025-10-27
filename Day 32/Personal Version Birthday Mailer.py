import random
import smtplib

MY_EMAIL = ""
PASSWORD=""

import pandas as pd
import datetime as dt



def send_email(to_addrs, email_template):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_addrs, msg=f"Happy Birthday!!\n\n {email_template}")
    except Exception as e:
        print(e)

df = pd.read_csv("birthdays.csv")


now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthday_people = df[(df['month'] == today_month) & (df['day'] == today_day)]

for index, row in birthday_people.iterrows():
    file_path = f"letter_templates/letter_{random.choice([1,2,3])}.txt"

    with open(file_path) as b_letter:
        contents = b_letter.read()
        contents = contents.replace("[NAME]", row["name"])

    send_email(row['email'], contents)


