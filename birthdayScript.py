import smtplib
from email.mime.text import MIMEText
import yagmail
import pandas as pd
import datetime

df = pd.read_csv(r'C:\Users\ronnie\birthday-calendar.csv')
df['Start Date'] = df['Start Date'].astype(str)

def extract_month(x):
    datee = datetime.datetime.strptime(x, "%m/%d/%Y")
    month = datee.month
    return month

def extract_day(x):
    datee = datetime.datetime.strptime(x, "%m/%d/%Y")
    day = datee.day
    return day

today = datetime.date.today().strftime("%m/%d/%Y")

df['Birthday'] = df['Start Date'].apply(lambda x: str(extract_month(x))+' '+str(extract_day(x)))

df['Y/N'] = df['Birthday'].apply(lambda x: 'Y' if x == str(extract_month(today))+' '+str(extract_day(today)) else 'N')

bdayDF = df[df['Y/N'] == 'Y']
bdaylst = bdayDF['Subject'].to_list()
bdaylst

receiver = 'ronaldmyers4@gmail.com'

body = "Today's people people are: "
for i in range(0, len(bdaylst)):
    body = body + '\n' + bdaylst[i]


yag = yagmail.SMTP('friendbday@gmail.com', 'Friendbday!1')
yag.send(
    to=receiver,
    subject="Today's Birthdays",
    contents=body
    #attachments=filename
)
