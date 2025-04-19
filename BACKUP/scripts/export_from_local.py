import os
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

# 環境變數
CLIENT_ID = os.getenv("GDRIVE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GDRIVE_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("GDRIVE_REFRESH_TOKEN")
TOKEN_URI = os.getenv("GDRIVE_TOKEN_URI")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
TARGET_FOLDER_ID = "1yA-KNuafM3zIao0pawbljWyKA2eiR2ON"

# 今日日期
today = datetime.now().strftime("%Y-%m-%d")

# 檔案路徑
json_path = "BACKUP/chat_backup.json"
md_path = f"BACKUP/backup_{today}.md"

# 讀 JSON + 轉 Markdown
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

lines = [f"# ChatGPT 對話備份 - {today}\n"]
for i, msg in enumerate(data.get("messages", [])):
    role = "User" if i % 2 == 0 else "Assistant"
    lines.append(f"### {role}\n{msg}\n")

with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# 驗證
creds = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri=TOKEN_URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

service = build("drive", "v3", credentials=creds)

# 上傳 JSON 檔案
def upload(file_path):
    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": [TARGET_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    return file.get("id")

json_id = upload(json_path)
md_id = upload(md_path)

# Discord 通知
file_url = f"https://drive.google.com/file/d/{json_id}"
message = {
    "content": f"✅ ChatGPT 備份完成！\n📅 {today}\n📦 檔案：chat_backup.json + .md\n🔗 [查看備份檔案]({file_url})\n🕒 自動時間：03:00"
}
res = requests.post(DISCORD_WEBHOOK, json=message)
if res.status_code == 204:
    print("✅ Discord 通知成功")
else:
    print("❌ Discord 通知失敗：", res.text)
