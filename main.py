##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

import datetime as dt
from os

now = dt.datetime.now()
today = (now.month, now.day)
print(today)

# HINT 2: Use pandas to read the birthdays.csv
import pandas
datas = pandas.read_csv('birthdays.csv')
print(datas)

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays = {
    (row["month"], row["day"]): {
        "name": row["name"],
        "email": row["email"],
        "year": row["year"],
    }
    for _, row in datas.iterrows()
}

print(birthdays)
for i in birthdays:
    print(i)



#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }



#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today in birthdays:
    name = birthdays[today]["name"]

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
import random

random = random.randint(1,3)
print(random)
if random == 1:
    with open("./letter_templates/letter_1.txt", "r") as a:
        list1 = a.read()
        new_letter = list1.replace("[NAME]", name)
if random == 2:
    with open("./letter_templates/letter_2.txt", "r") as b:
        list2 = b.read()
        new_letter = list2.replace("[NAME]", name)
if random == 3:
    with open("./letter_templates/letter_3.txt", "r") as c:
        list3 = c.read()
        new_letter = list3.replace("[NAME]", name)
print(new_letter)


# 4. Send the letter generated in step 3 to that person's email address.


import smtplib

to_email = birthdays[today]["email"]
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg=f"Subject:Hello\n\n{new_letter}"
    )




