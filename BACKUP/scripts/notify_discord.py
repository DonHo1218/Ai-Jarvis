import requests
import os
from datetime import datetime

# 從環境變數讀取 Webhook（GitHub Secrets）
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
GOOGLE_DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")

today = datetime.now().strftime("%Y-%m-%d")
folder_url = f"https://drive.google.com/drive/folders/{GOOGLE_DRIVE_FOLDER_ID}"

message = {
    "content": f"✅ ChatGPT 備份完成！\n📅 {today}\n📦 備份資料夾：\n🔗 [立即查看]({folder_url})\n🕛 自動時間：12:00"
}

res = requests.post(WEBHOOK_URL, json=message)

if res.status_code == 204:
    print("✅ Discord 通知成功")
else:
    print("❌ Discord 通知失敗：", res.text)
