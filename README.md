# Facebook to Google Sheets Automation 📊

This Python script automates the process of extracting post performance data from a Facebook Page (via the Graph API) and writing it into a Google Sheet.
It fetches post links, publish dates, reach, impressions, and engagement metrics—making it easy to analyze performance, track trends, or archive data for reporting.
Ideal for digital marketers, content managers, and analysts who want a lightweight, code-driven solution without relying on paid automation platforms.

## 📌 Features
- Pulls post link, creation date, impressions, reach, and engagement
- Automatically writes them into a Google Spreadsheet

## 🛠️ Setup

### 1. Google Sheets API
- Create a Google Cloud Project
- Enable the Google Sheets API
- Create a service account and download the `.json` credentials file
- Share the target Google Sheet with the service account email

### 2. Facebook Graph API
- Create a Facebook App
- Obtain a Page Access Token with `pages_read_engagement` permission
- Note your Page ID

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Run
```bash
python facebook_to_sheets.py
```
### ⚠️ Disclaimer
Facebook API access is subject to change and may require additional app reviews or permissions.

### 🙌 Contribution
Feel free to fork, improve, and PR!
---
