from twilio.rest import Client
import pandas as pd
import datetime

import os
from dotenv import load_dotenv
load_dotenv()

# Load Twilio credentials
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("FROM_WHATSAPP")
TO_WHATSAPP = os.getenv("TO_WHATSAPP")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_daily_reminders():
    df = pd.read_csv("kalnirnay_2025.csv")
    df['date'] = pd.to_datetime(df['date']).dt.date
    today = datetime.date.today()
    events_today = df[df['date'] == today]

    for _, row in events_today.iterrows():
        msg = f"📿 *{row['event']}* is today!\n🗓️ {row['description']}"
        message = client.messages.create(
            from_=FROM_WHATSAPP,
            to=TO_WHATSAPP,
            body=msg
        )
        print(f"Sent reminder: {msg}")

send_daily_reminders()
