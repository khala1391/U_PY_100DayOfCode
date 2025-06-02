from datetime import datetime
import pandas as pd
import random
import smtplib
import pprint
import json

MY_EMAIL ="k@gmail.com"
MY_PASSWORD = "xxxx xxxx xxxx xxxx"

# ----------------------------------------------------
now = datetime.now()
today = (now.month, now.day)
 
# df = pd.read_csv("day32/birthday-wisher/birthdays.csv")
df = pd.read_csv("birthdays.csv")
birthdays_dict = df.to_dict(orient="records")
 
for birthday in birthdays_dict:
    month_day_birth = (birthday['month'], birthday['day'])
    birthday_name = birthday['name']
    birthday_email = birthday['email']
    birthday_year = birthday['year']
    birthday_date = (birthday_year, birthday['month'], birthday['day'])
    random_letter = random.randint(1, 3)
    # letter_file = "day32/birthday-wisher/letter_templates/letter_{}.txt".format(random_letter)
    letter_file = "letter_templates/letter_{}.txt".format(random_letter)
    if today == month_day_birth:
        with open(letter_file) as f:
            content = f.read()
            content = content.replace("[NAME]", birthday_name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg= f"Subject: Happy Birthday_test \n\n {content}")
            print(f"HBD to {birthday_name} have been submitted")


