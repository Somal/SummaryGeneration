import gspread
from oauth2client.service_account import ServiceAccountCredentials


def login():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_id.json', scope)
    gc = gspread.authorize(credentials)
    return gc


def create_spreadsheet(data: dict):
    pass