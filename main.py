#layout of actual game and things run
from __future__ import print_function
from menu import *
from help import *
from gameA import *
from gameB import *
from math import *
from random import *


running = True

curScreen = "menu" #menu, help, game, and end

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Bad Gamey Circles 25-9664c3ab308c.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Bad Gamey Circle 2.5").sheet1

while running:

    if curScreen == "menu":
        curScreen = dispMenu()

    elif curScreen == "help":
        curScreen = dispOptions()

    elif curScreen == "game":
        nGames = int(sheet.cell(1, 1).value)  # Number of games that are currently running
        nGames += 1
        sheet.update_cell(1, 1, str(nGames))  # Update the number of games opened


        # each individual user has their own unique id
        # Determine whether the user is team A or team B (Whoever is first is Team A)
        # Cell (ID,2) stores the status of the user
        row = 2
        ID = 1
        flag = False #Whether there are players waiting to be played
        while sheet.cell(row, 1).value!= "":       #Finding an open game
            if sheet.cell(row,2).value=="A":
                flag = True

            row+=200         #Reserve 200 rows for storing data of troops
            ID +=1
        sheet.update_cell(row, 1, str(ID))
        if flag:
            sheet.update_cell(row, 2, "B")
            curScreen = dispGameA()

        else:
            sheet.update_cell(row, 2, "A")
            curScreen = dispGameB()



        # curScreen = dispGameA() and dispGameB()

    elif curScreen == "end":

        # Add delete rows of data
        # Supports maximum of 5 games opened (200 rows of data per game opened)
        nGames-=1
        sheet.update_cell(1,1,str(nGames))
        break


    else:
        running = False


quit()







