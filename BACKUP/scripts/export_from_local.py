import json
from datetime import datetime

input_path = "BACKUP/chat_backup.json"
output_path = f"BACKUP/backup_{datetime.now().strftime('%Y-%m-%d')}.md"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

messages = data.get("messages", [])
lines = [f"# ChatGPT 對話備份 - {datetime.now().strftime('%Y-%m-%d')}\n"]

for i, msg in enumerate(messages):
    role = "User" if i % 2 == 0 else "Assistant"
    lines.append(f"### {role}:\n{msg}\n")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("✅ Markdown 匯出完成")
