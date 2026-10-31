from wifi_connect import wifi_loop
from telegram import send_telegram

# Settings
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN for this esp "
TELEGRAM_CHAT_ID = "8368702577" # sam chat id (personal)

DEVICE_ID = "ESP_TEST"

# Connect to Wi-Fi
wifi_loop(WIFI_SSID, WIFI_PASSWORD)

# Send notification
send_telegram(
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    DEVICE_ID,
    "Hello! This is a test notification from my ESP32."
)

print("Telegram notification sent!")