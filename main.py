from datetime import datetime
import pandas as pd
import random
import smtplib

my_email = "your email here"
my_password = "your password here"

today = (datetime.now().month, datetime.now().day)
data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        name = birthday_person["name"]        
        content = content.replace("[NAME]",name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! \n \n {content}"
            )
    print("Email sent successfully! ")


