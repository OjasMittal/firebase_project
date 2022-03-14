import yagmail
import pandas
from newsfeed import NewsFeed
import datetime
import time


def send_email(row):

      today = datetime.datetime.now().strftime('%Y-%m-%d')
      yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
      news_feed = NewsFeed(interest=row['Interest'],
                           from_date=yesterday,
                           to_date=today)
      email = yagmail.SMTP(user="automail.ojas.python@gmail.com", password="pffqjjkczoyvahtv")
      email.send(to=row['Email'],
                 subject=f"Your {row['Interest']} news for today!",
                 contents=f"Hi {row['Name']} \n See what's on about {row['Interest']} today. \n{news_feed.get()}")
      return ("Success")

if __name__=="__main__":
    ef = pandas.read_excel("people.xlsx")
    for index, row in ef.iterrows():
        print(send_email())






