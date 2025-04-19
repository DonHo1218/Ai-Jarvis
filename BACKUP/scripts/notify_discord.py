import requests
import os
from datetime import datetime

# 讀取環境變數
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
GOOGLE_DRIVE_FILE_ID = os.getenv("GOOGLE_DRIVE_FILE_ID")

# ✅ 防呆處理：無 Webhook URL 就 raise error
if not WEBHOOK_URL:
    raise ValueError("❌ 未設定 DISCORD_WEBHOOK_URL！請檢查 GitHub Secrets")

if not GOOGLE_DRIVE_FILE_ID:
    raise ValueError("❌ 未設定 GOOGLE_DRIVE_FILE_ID！請檢查 GitHub Secrets")

# 組裝訊息
today = datetime.now().strftime("%Y-%m-%d")
file_url = f"https://drive.google.com/file/d/{GOOGLE_DRIVE_FILE_ID}"

message = {
    "content": f"✅ ChatGPT 備份完成！\n📅 {today}\n📦 備份資料夾：\n🔗 [立即查看]({file_url})\n🕛 自動時間：12:00"
}

# 發送到 Discord
res = requests.post(WEBHOOK_URL, json=message)

if res.status_code == 204:
    print("✅ Discord 通知成功")
else:
    print("❌ Discord 通知失敗：", res.text)
