import pandas
import random
import datetime as dt
import smtplib

today = dt.datetime.now()
day = today.day
month = today.month
# User_id and password of your email services Use app password option for gmail because google now do not support less
# secure option to run third party application for app password option you must enable the 2 steps verification option

MY_EMAIL = "xoxozoo1992@gmail.com"
MY_PASSWORD = "yvytososmfdpassd"

with open("birthdays.csv") as bt:
    birth_data = pandas.read_csv(bt)
    birth_data_dic = birth_data.to_dict()
    for i in range(len(birth_data_dic["name"])):
        m = birth_data_dic["month"][i]
        d = birth_data_dic["day"][i]
        n = birth_data_dic["name"][i]
        e = birth_data_dic["email"][i]
        if m == month and d == day:
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
                ready_file = file.read()
                send_file = ready_file.replace("[NAME]", n)

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL, MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Happy Birthday!\n\n{send_file}"
                    )
        else:
            break









