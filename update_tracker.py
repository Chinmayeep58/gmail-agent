import json
import os
from datetime import datetime

from gmail_reader import get_recent_emails
from status_classifier import detect_status
from company_extractor import extract_company
from job_filter import is_job_email


DB_FILE = "applications.json"


def load_db():

    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_applications():

    apps = load_db()

    emails = get_recent_emails()

    for email in emails:

        subject = email["subject"]
        snippet = email["snippet"]

        # 🚨 FILTER NON JOB EMAILS
        if not is_job_email(subject, snippet):
            continue

        text = subject + " " + snippet

        company = extract_company(email['subject'], email["sender"])

        if not company:
            continue

        status = detect_status(text)

        existing = None

        for app in apps:
            if app["company"].lower() == company.lower():
                existing = app
                break

        if existing:

            if status != "Pending":
                existing["status"] = status

        else:

            apps.append({
                "company": company,
                "status": status if status != "Pending" else "Applied",
                "source_email": subject,
                "date_detected": str(datetime.today().date())
            })

    save_db(apps)


if __name__ == "__main__":
    update_applications()