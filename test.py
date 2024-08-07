import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Load credentials
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/dell/Downloads/telegram-431711-da3931bfa3c3.json', scope)

# Authorize and connect to Google Sheets
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open("Telegrambot").sheet1

# Fetch and print data from the sheet
data = sheet.get_all_records()
print(data)
