# Gmail Job Application Tracker

Last Updated: March 2026

## Overview

The **Gmail Job Application Tracker** is a lightweight tool that automatically tracks job applications by scanning Gmail emails and identifying application-related messages.

The system extracts relevant information such as:

* Company name
* Application status
* Application date
* Detection date

The results are displayed in an interactive **Streamlit dashboard**, allowing users to track the progress of their job applications in a single place.

This project demonstrates how **email scraping, rule-based classification, and lightweight automation** can be used to build a practical productivity tool.

Author: Chinmayee
GitHub Profile: https://github.com/Chinmayeep58

---

## System Architecture

The system follows a simple processing pipeline:

Gmail Inbox
↓
Gmail API Reader
↓
Job Email Filter
↓
Company Extraction
↓
Status Classification
↓
Application Tracker Database
↓
Streamlit Dashboard

Each component performs a specific function:

* **gmail_reader.py** — Reads recent emails using the Gmail API
* **job_filter.py** — Filters only job-related emails
* **company_extractor.py** — Extracts company names from email metadata
* **status_classifier.py** — Determines the application stage (Applied, Interview, etc.)
* **update_tracker.py** — Updates the application database
* **app.py** — Displays the dashboard

---

## Recommendation / Classification Logic

Instead of using an AI model, the system uses **rule-based classification**.

Examples of signals used:

Email phrases:

* "Thank you for applying"
* "Application received"
* "Interview invitation"
* "Unfortunately we will not move forward"

These signals help classify the application into stages:

Applied
Assessment
Interview
Offer
Rejected

This design makes the system **simple, transparent, and cost-free to run**.

---

## Quality of Recommendation
In this project, feedback is supported through:

Manual application entries
Manual status updates
Verification of automatically detected applications

These corrections can be used to:

* Improve keyword detection
* Refine filtering logic
* Enhance company extraction rules

Future versions could incorporate **machine learning models** to improve classification accuracy.

---

## Installation

### 1. Clone the repository

git clone https://github.com/Chinmayeep58/gmail-agent.git
cd gmail-agent

---

### 2. Create a virtual environment

python -m venv venv

Activate environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Configure Gmail API

1. Go to Google Cloud Console
2. Enable Gmail API
3. Create OAuth credentials
4. Download credentials.json and place it in the project root

Do NOT commit credentials.json to GitHub.

---

### 5. Run the application

streamlit run app.py

The dashboard will open in your browser.

---

## Data Sources

This project uses:

Gmail API (Google Cloud)

Documentation:
https://developers.google.com/gmail/api

No email data is stored or distributed in this repository.

---

## Features

Automatic Gmail scanning
Application status classification
Company detection
Manual application tracking
Interactive dashboard
Local JSON database storage

---

## Future Enhancements

Possible improvements include:

AI-based email classification
Interview date extraction
Calendar integration
Automated status updates from new emails
Support for multiple email providers
Improved company extraction using NLP
Application analytics dashboard

---

## Collaboration

Contributions are welcome.

You may:

* Fork the repository
* Suggest improvements
* Submit pull requests
* Extend the project with new features

If you are interested in collaborating, feel free to open an issue or contact me.

---

## Repository Guidelines

This repository intentionally excludes:

credentials.json
token.pickle
.env files

These files contain sensitive credentials and should not be committed.

---

## References

Gmail API Documentation
https://developers.google.com/gmail/api

Streamlit Documentation
https://docs.streamlit.io

Python JSON Documentation
https://docs.python.org/3/library/json.html

---

## License

This project is open for learning and experimentation.
