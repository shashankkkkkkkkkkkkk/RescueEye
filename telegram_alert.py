import requests
from config import BOT_TOKEN, CHAT_ID

def send_telegram_alert(image_path, survivor_number):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    caption = f"🚨 Survivor Detected!\nSurvivor #{survivor_number}\n📸 Evidence Attached"

    with open(image_path, "rb") as photo:
        response = requests.post(
            url,
            data={"chat_id": CHAT_ID, "caption": caption},
            files={"photo": photo}
        )

    print("📩 Telegram Response:", response.text)
