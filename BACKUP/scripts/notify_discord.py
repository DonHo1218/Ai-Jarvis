import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(message):
    if not DISCORD_WEBHOOK_URL:
        print("⚠️ 未設定 DISCORD_WEBHOOK_URL，已略過通知。")
        return

    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"❌ 發送失敗: {response.status_code} - {response.text}")
    else:
        print("✅ Discord 通知已成功送出。")

if __name__ == "__main__":
    send_discord_message("✅ ChatGPT 備份已完成。")
