import PySimpleGUI as sg
import subprocess
import validators
from string import whitespace
from playsound import playsound
import winsound
import os

import layouts.mainMenu as mainMenu
import layouts.inputMenu as inputMenu
import layouts.downloadMenu as downloadMenu


version = '0.1.0'
sg.theme('DarkAmber')

steamcmdDir = ""
outputDir = ""
links = []


def isValidInput(link):
    if validators.url(link) == True:
        return True
    else:
        return False

def downloadMods(modList):
    for x in modList:
        if isValidInput(x) == True:
            x.translate(dict.fromkeys(map(ord, whitespace)))
            workshopId = x.split("=")[-1]
            workshopId = workshopId.strip('\n')
            cmd = "{steamcmdDirectory}\\steamcmd.exe +force_install_dir {outputDirectory} +login anonymous +workshop_download_item 294100 {id} +quit".format(steamcmdDirectory=steamcmdDir, outputDirectory=outputDir, id=workshopId)
            subprocess.run(cmd, shell=True)
            
            


metaLayout = [
                [sg.Column(mainMenu.mainMenuLayout, key='-COL1-'),
                sg.Column(inputMenu.inputMenuLayout, visible=False, key='-COL2-'),
                sg.Column(downloadMenu.downloadMenuLayout, visible=False, key='-COL3-')]
             ]

window = sg.Window(title=('Workshop Downloader v' + version), layout=metaLayout, margins=(10, 10))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or 'Exit' in event:  # If window is closed or user presses any Exit button (events must be unique so it adds a 1 to the event name)
        break
    if event == 'Back':
        window['-COL1-'].update(visible=True)
        window['-COL2-'].update(visible=False)
        window['-COL3-'].update(visible=False)
        window['-IN-'].update('')
        
    if event == 'Next':
        steamcmdDir = values[0] # Grabbing values from the folder pickers
        outputDir = values[1]
        if steamcmdDir != "" and "steamcmd.exe" in os.listdir(steamcmdDir) and outputDir != "":
            window['-COL1-'].update(visible=False)
            window['-COL2-'].update(visible=True)
            window['-COL3-'].update(visible=False)
        else:
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
            sg.popup('Please select a valid SteamCMD install directory and an output directory')
            
    if event == 'DOWNLOAD':
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=False)
        window['-COL3-'].update(visible=True)
        links = values['-IN-'].splitlines()
        downloadMods(links)
        playsound('beep.mp3')
        
    if event == '-OUTPUT-':
        if outputDir != "" and outputDir != None:
            subprocess.run('start ' + outputDir + ' /max', shell=True)
        else:
            sg.popup('No output directory selected!')
    
        

window.close()
