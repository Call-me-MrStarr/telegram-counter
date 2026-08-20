import os
import urllib.request
import urllib.parse
import json
from datetime import date

# ==========================
# تنظیمات روزشمار
# ==========================

BASE_DATE = date(2026, 8, 20)
BASE_NUMBER = 927

# ==========================
# اطلاعات ربات
# این‌ها را بعداً در GitHub Secrets قرار می‌دهیم
# ==========================

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
GIF = os.environ["GIF"]


def get_day_number():
    today = date.today()
    days_passed = (today - BASE_DATE).days
    return BASE_NUMBER + days_passed


def send_gif():
    day_number = get_day_number()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendAnimation"

    data = {
        "chat_id": CHANNEL_ID,
        "animation": GIF,
        "caption": f"📅 روز {day_number}"
    }

    encoded_data = urllib.parse.urlencode(data).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=encoded_data,
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    if result.get("ok"):
        print(f"✅ روز {day_number} با موفقیت ارسال شد.")
    else:
        print("❌ ارسال ناموفق بود:")
        print(result)


if __name__ == "__main__":
    send_gif()
