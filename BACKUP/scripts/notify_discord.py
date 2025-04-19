import requests
import os
from datetime import datetime

# 從環境變數讀取 Webhook（GitHub Secrets）
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
GOOGLE_DRIVE_FILE_ID = os.getenv("GOOGLE_DRIVE_FILE_ID")  # 如果你想靈活啲

today = datetime.now().strftime("%Y-%m-%d")
file_url = f"https://drive.google.com/file/d/{GOOGLE_DRIVE_FILE_ID}"

message = {
    "content": f"✅ ChatGPT 備份完成！\n📅 {today}\n📦 檔案：chat_backup.json + .md\n🔗 [查看備份檔案]({file_url})\n🕛 自動時間：12:00"
}

res = requests.post(WEBHOOK_URL, json=message)

if res.status_code == 204:
    print("✅ Discord 通知成功")
else:
    print("❌ Discord 通知失敗：", res.text)
