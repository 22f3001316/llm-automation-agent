import json
import os
import subprocess
import sqlite3
from datetime import datetime
from pathlib import Path
from src.llm_handler import call_llm
from src.utils import write_file, read_file, find_most_similar
from PIL import Image
import pytesseract

DATA_DIR = Path("/data")

def process_task(task: str):
    if "install uv" in task:
        subprocess.run(["pip", "install", "uv"], check=True)
    elif "format markdown" in task:
        subprocess.run(["npx", "prettier", "--write", str(DATA_DIR / "format.md")], check=True)
    elif "count wednesdays" in task:
        dates = (DATA_DIR / "dates.txt").read_text().splitlines()
        count = sum(1 for d in dates if datetime.strptime(d, "%Y-%m-%d").weekday() == 2)
        write_file("dates-wednesdays.txt", str(count))
    elif "sort contacts" in task:
        contacts = json.loads(read_file("contacts.json"))
        contacts.sort(key=lambda x: (x['last_name'], x['first_name']))
        write_file("contacts-sorted.json", json.dumps(contacts, indent=2))
    elif "extract logs" in task:
        logs = sorted(DATA_DIR.glob("logs/*.log"), key=os.path.getmtime, reverse=True)[:10]
        first_lines = [log.open().readline().strip() for log in logs]
        write_file("logs-recent.txt", "\n".join(first_lines))
    elif "index markdown files" in task:
        index = {}
        for md_file in DATA_DIR.glob("docs/*.md"):
            lines = md_file.read_text().splitlines()
            title = next((line[2:] for line in lines if line.startswith("# ")), "")
            index[md_file.name] = title
        write_file("docs/index.json", json.dumps(index, indent=2))
    elif "extract email sender" in task:
        email_content = read_file("email.txt")
        sender = call_llm(f"Extract sender email from: {email_content}")
        write_file("email-sender.txt", sender)
    elif "extract credit card" in task:
        img = Image.open(DATA_DIR / "credit-card.png")
        card_number = pytesseract.image_to_string(img).replace(" ", "")
        write_file("credit-card.txt", card_number)
    elif "find similar comments" in task:
        comments = read_file("comments.txt").splitlines()
        most_similar = find_most_similar(comments)
        write_file("comments-similar.txt", "\n".join(most_similar))
    elif "total sales of Gold tickets" in task:
        conn = sqlite3.connect(DATA_DIR / "ticket-sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type='Gold'")
        total_sales = cursor.fetchone()[0]
        write_file("ticket-sales-gold.txt", str(total_sales))
        conn.close()
    else:
        raise ValueError("Unknown task")
