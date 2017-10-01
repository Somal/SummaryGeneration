# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import httplib2
# import apiclient.discovery
#
#
# def login():
#     scope = ['https://spreadsheets.google.com/feeds']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('client_id.json', scope)
#     gc = gspread.authorize(credentials)
#     return gc
#
#
# def create_spreadsheet(data: dict):
#     gc = login()
#     # gc.open_by_key('1UElMY3STL3PFROdCNqj3KkGXy3XybbrV6E1-InWL4Mg')
#     gc.create('Smth')
#     # spread = gc.open('Итоги недели 25.09.2017-01.10.2017')
#
#
# if __name__ == '__main__':
#     # create_spreadsheet({})
#     CREDENTIALS_FILE = 'client_id.json'  # имя файла с закрытым ключом
#
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
#                                                                    ['https://www.googleapis.com/auth/spreadsheets',
#                                                                     'https://www.googleapis.com/auth/drive'])
#     httpAuth = credentials.authorize(httplib2.Http())
#     service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
#
#     spreadsheet = service.spreadsheets().create(body={
#         'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
#         'sheets': [{'properties': {'sheetType': 'GRID',
#                                    'sheetId': 0,
#                                    'title': 'Сие есть название листа',
#                                    'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
#     }).execute()
