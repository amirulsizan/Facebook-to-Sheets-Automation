# Facebook to Google Sheets Automation 📊

This Python script automates the process of extracting post performance data from a Facebook Page (via the Graph API) and writing it into a Google Sheet.

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
Let me know if you want me to zip this up for download or walk you through publishing the repo on GitHub. I can help you name it, write a good project description, or even draft a license file if you want to open-source it.
