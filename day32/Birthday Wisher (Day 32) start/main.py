import smtplib
import datetime as dt
import random
import pandas as pd

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_email", password="your_password")
        connection.sendmail(from_addr="your_email", to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday {birthday_person['name']}! \n\n {contents}")
