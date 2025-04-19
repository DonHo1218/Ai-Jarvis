import os
import json
from datetime import datetime

json_file = "BACKUP/chat_backup.json"
md_file = f"BACKUP/backup_{datetime.now().strftime('%Y-%m-%d')}.md"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

lines = [f"# ChatGPT 對話備份 - {datetime.now().strftime('%Y-%m-%d')}\n"]

for i, msg in enumerate(data["messages"]):
    role = "User" if i % 2 == 0 else "Assistant"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines.append(f"### [{timestamp}] {role}\n")
    lines.append(msg.strip())
    lines.append("")

with open(md_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("✅ 轉換成功")
