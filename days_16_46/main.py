from datetime import datetime
import pandas
import random
import smtplib

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")


#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login()
        connection.sendmail(
            from_addr="",
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"

        )




