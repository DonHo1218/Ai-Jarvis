import json
import os

def main():
    input_path = "BACKUP/data/chat_backup.json"
    output_dir = "BACKUP/data"

    if not os.path.exists(input_path):
        print(f"❌ 找不到來源檔案：{input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    date = data.get("date")
    if not date:
        print("❌ JSON 檔案缺少 'date' 欄位")
        return

    filename = f"chat_backup_{date}.json"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

    print(f"✅ 備份完成：{output_path}")

if __name__ == "__main__":
    main()
