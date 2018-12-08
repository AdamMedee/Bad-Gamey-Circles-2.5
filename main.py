#layout of actual game and things run
from __future__ import print_function
from pygame import *
from math import *
from random import *
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

init()

WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT))

running = True

leftClick, middleClick, rightClick = False, False, False
scroll = 0
mousePos = (0, 0)
menu = "menu" #menu, help, game, and end

"""
#Google sheets stuff
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        print('%s, %s' % (row[0], row[4]))
"""

while running:
    leftClick, middleClick, rightClick = False, False, False
    scroll = 0
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

    if menu == "menu":
        pass

    elif menu == "help":
        pass

    elif menu == "game":
        pass

    elif menu == "end":
        pass

    else:
        print("???")

    display.flip()
quit()







