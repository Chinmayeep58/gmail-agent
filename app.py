import streamlit as st
import json
import pandas as pd
from datetime import datetime
from update_tracker import update_applications

DB_FILE = "applications.json"

st.title("Job Application Tracker")

# -----------------------------
# Gmail Sync
# -----------------------------

if st.button("Sync Gmail"):
    update_applications()
    st.success("Tracker updated from Gmail!")

# -----------------------------
# Load Database
# -----------------------------

try:
    with open(DB_FILE) as f:
        apps = json.load(f)
except:
    apps = []

# -----------------------------
# Manual Entry
# -----------------------------

st.subheader("+ Add Application Manually")

company_input = st.text_input("Company Name")

application_date = st.date_input(
    "Application Date",
    value=datetime.today()
)

status_options = [
    "Applied",
    "Assessment",
    "Interview",
    "Offer",
    "Rejected"
]

status_input = st.selectbox(
    "Application Status",
    status_options
)

if st.button("Add Application"):

    if company_input.strip() != "":

        new_entry = {
            "company": company_input.strip(),
            "status": status_input,
            "application_date": str(application_date),
            "date_detected": str(datetime.today().date()),
            "source_email": "Manual Entry"
        }

        apps.append(new_entry)

        with open(DB_FILE, "w") as f:
            json.dump(apps, f, indent=4)

        st.success("Application added!")

# -----------------------------
# Display Applications
# -----------------------------

st.subheader("Tracked Applications")

if len(apps) == 0:

    st.write("No applications tracked yet.")

else:

    df = pd.DataFrame(apps)

    df = df.rename(columns={
        "company": "Company",
        "status": "Status",
        "application_date": "Applied On",
        "date_detected": "Detected On"
    })

    columns_to_show = ["Company", "Status", "Applied On", "Detected On"]

    df = df[[col for col in columns_to_show if col in df.columns]]

    st.table(df)
