import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "drajner22@gmail.com"
MY_PASSWORD = "clvbvcersotzxkbv"


now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
month_list = data["month"].to_list()
day_list = data["day"].to_list()
name_list = data["name"].to_list()
emails_list = data["email"].to_list()

for i in range(0, len(month_list)):
    if month == month_list[i]:
        if day == day_list[i]:
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            with open(file_path) as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", name_list[i])

            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=emails_list[i],
                    msg=f"Subject:Happy BirthDay\n\n{contents}"
                )
