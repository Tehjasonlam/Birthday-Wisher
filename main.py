import smtplib
import datetime as dt
import random
import pandas

my_email = "fill in your email"
password ="fill in your password"

now = dt.datetime.now()
month = now.month
day = now.day

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
for person in birthdays:
    if person["day"] == day and person["month"] == month:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
        email = person["email"]
        name = person["name"]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
        finished_letter = letter.replace("[NAME]", name)


        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()  # secure connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday Day\n\n{finished_letter}")