import smtplib
import datetime as dt
import random

MY_EMAIL ="khala1391@gmail.com"
MY_PASSWORD = "xnmp nkpp fcte rjty"

now = dt.datetime.now()
weekday = now.weekday()
# if weekday == 0:
if weekday == 5:
    with open("day32/quote/quotes.txt") as f:
        all_quotes= f.readlines()
        quote = random.choice(all_quotes)
    
    # print(quote)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="khala1391@hotmail.com",
                            msg= f"Subject: Monday Motivation \n\n {quote}")
    
    
    
    
    

    

# # step
# get current day of the week (change to Monday later)
# create list from quote.txt
# use random module to get quote
# us smtplib to send email

    
    