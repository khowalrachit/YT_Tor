import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('yt-torrent-e5e42df414e4.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open("YT_Tor").worksheet("YT_Tor")
request_data = spreadsheet.cell('1','3').value

print(request_data)

                                                               
