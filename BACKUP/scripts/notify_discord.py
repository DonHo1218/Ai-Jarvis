import requests
from datetime import datetime

# ⚠️ 改呢個 ID 成為真正 Google Drive 回傳 ID
GOOGLE_DRIVE_FILE_ID = "1ABCDEF123456XYZ"
WEBHOOK_URL = "https://discord.com/api/webhooks/..."

today = datetime.now().strftime("%Y-%m-%d")
file_url = f"https://drive.google.com/file/d/{GOOGLE_DRIVE_FILE_ID}"

message = {
    "content": f"✅ ChatGPT 備份完成！\n📅 {today}\n📦 檔案：chat_backup.json + .md\n🔗 [查看備份檔案]({file_url})\n🕒 自動時間：03:00"
}

res = requests.post(WEBHOOK_URL, json=message)

if res.status_code == 204:
    print("✅ Discord 通知成功")
else:
    print("❌ Discord 通知失敗：", res.text)
