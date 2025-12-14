##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib


sender = "YOUR_GMAIL_ADDRESS"
password = "YOUR_APP_PASSWORD"

templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    receiver = birthday_dict[today_tuple]["email"]
    birthday_person = birthday_dict[today_tuple]["name"]
    template = random.choice(templates)
    with open(file=f"letter_templates/{template}") as file:
        file_data = file.read()
        file_data = file_data.replace("[NAME]", birthday_person)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=receiver,
                msg=f"subject: Happy Birthday\n\n{file_data}"
            )