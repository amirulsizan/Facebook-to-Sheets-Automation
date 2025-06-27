import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('your-creds-file.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Facebook Insights").sheet1

# Facebook API setup
access_token = 'your-facebook-access-token'
page_id = 'your-page-id'
fields = 'id,permalink_url,created_time,insights.metric(post_impressions,post_impressions_unique,post_engaged_users)'
url = f'https://graph.facebook.com/v19.0/{page_id}/posts?fields={fields}&access_token={access_token}'

# Fetch posts data
response = requests.get(url).json()
posts = response.get('data', [])

# Prepare and write data to Google Sheet
sheet.update('A1', [['Link', 'Date', 'Reach', 'Impressions', 'Engagement']])
for idx, post in enumerate(posts, start=2):
    link = post.get('permalink_url', '')
    created_time = datetime.strptime(post.get('created_time', ''), '%Y-%m-%dT%H:%M:%S%z').date()
    
    metrics = {m['name']: m['values'][0]['value'] for m in post.get('insights', {}).get('data', [])}
    reach = metrics.get('post_impressions_unique', 0)
    impressions = metrics.get('post_impressions', 0)
    engagement = metrics.get('post_engaged_users', 0)

    sheet.update(f'A{idx}:E{idx}', [[link, str(created_time), reach, impressions, engagement]])
