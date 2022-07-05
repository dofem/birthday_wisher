import smtplib
from random import *
import datetime as dt

with open("quotes.txt") as quote:
    quote = quote.readlines()
    quote_of_day = choice(quote)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    to_email = "femdarl@yahoo.com,dallyoluwafemi@gmail.com"

    my_email = "femdarl111@gmail.com"
    password = "rbfosxwkttmismxk"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email.split(","),
                        msg=f"subject:MOTIVATION\n\n{quote_of_day}")
else:
    print("today isnt motivation monday joorh")