import yagmail
import pandas
from news import newsDaily
import datetime
import time
h = datetime.datetime.now()
while True:
    if h.hour == 11 and h.minute == 1:
        df = pandas.read_excel('email.xlsx')

        for index, row in df.iterrows():
            today = h.strftime('%Y-%m-%%d')
            yest = (h - datetime.timedelta(days = 1)).strftime('%Y-%m-%%d')
            dailyNews = newsDaily(interest=row['interest']),from_date = yest, to_date = today)
            email = yagmail.SMTP(user="youremail@gmail.com", password="yourpassword")
            email.send(to=row['email'], subject = f"Your {row['interest']} for today!",
                       contents=f"Hey {row['name']}\n See what today's {row['interest']} news is. \n{dailyNews.get()}\nArdit")
            
    time.sleep(60)
