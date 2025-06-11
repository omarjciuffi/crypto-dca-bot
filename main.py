import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

while True:
    send_message("🔁 Reminder: controlla il tuo piano DCA settimanale!")
    time.sleep(60 * 60 * 24 * 7)  # ogni settimana

