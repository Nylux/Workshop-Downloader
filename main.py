import PySimpleGUI as sg
import subprocess
import validators
from string import whitespace
from playsound import playsound
import winsound
import os
import requests
from zipfile import ZipFile

import layouts.mainMenu as mainMenu
import layouts.inputMenu as inputMenu
import layouts.downloadMenu as downloadMenu
import layouts.steamcmdMenu as steamcmdMenu





version = '0.1.0'
sg.theme('DarkAmber')

steamcmdDir = ""
outputDir = ""
links = []

def installSteamcmd(path):
    response = requests.get("https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip", stream=True, allow_redirects=True)
    with open(path + "/steamcmd.zip", "wb") as handle:
        for data in response.iter_content():
            handle.write(data)
    with ZipFile(str(path) + "/steamcmd.zip", 'r') as zipObj:
        zipObj.extractall(path)
    os.remove(path + "/steamcmd.zip")
    
    
    

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
                [sg.Column(mainMenu.mainMenuLayout, key='-MAIN-'),
                sg.Column(inputMenu.inputMenuLayout, visible=False, key='-INPUT-'),
                sg.Column(downloadMenu.downloadMenuLayout, visible=False, key='-DOWNLOAD-'),
                sg.Column(steamcmdMenu.steamcmdMenuLayout, visible=False, key='-STEAMCMDMENU-')
             ]]

window = sg.Window(title=('Workshop Downloader v' + version), layout=metaLayout, margins=(10, 10))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or 'Exit' in event:  # If window is closed or user presses any Exit button (events must be unique so it adds a 1 to the event name)
        break
    if 'Back' in event:
        window['-MAIN-'].update(visible=True)
        window['-INPUT-'].update(visible=False)
        window['-DOWNLOAD-'].update(visible=False)
        window['-STEAMCMDMENU-'].update(visible=False)
        window['-IN-'].update('') # Clear input field when we change windows
        
    if event == 'Next':
        steamcmdDir = values[1] # Grabbing values from the folder pickers # THIS IS BAD, SHOULD USE KEYS INSTEAD
        outputDir = values[2]
        if steamcmdDir != "" and "steamcmd.exe" in os.listdir(steamcmdDir) and outputDir != "":
            window['-MAIN-'].update(visible=False)
            window['-INPUT-'].update(visible=True)
            window['-DOWNLOAD-'].update(visible=False)
            window['-STEAMCMDMENU-'].update(visible=False)
        else:
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
            sg.popup('Please select a valid SteamCMD install directory and an output directory')
            
    if event == 'DOWNLOAD':
        window['-MAIN-'].update(visible=False)
        window['-INPUT-'].update(visible=False)
        window['-DOWNLOAD-'].update(visible=True)
        window['-STEAMCMDMENU-'].update(visible=False)
        links = values['-IN-'].splitlines()
        downloadMods(links)
        playsound('beep.mp3')
        
    if event == '-OUTPUT-':
        if outputDir != "" and outputDir != None:
            os.startfile(outputDir)
        else:
            sg.popup('No output directory selected!')
    
    if event == '-STEAMCMD-':
        window['-MAIN-'].update(visible=False)
        window['-INPUT-'].update(visible=False)
        window['-DOWNLOAD-'].update(visible=False)
        window['-STEAMCMDMENU-'].update(visible=True)
    
    if event == '-DOWNLOAD_STEAMCMD-':
        if values['-STEAMCMD_INSTALL_FOLDER-'] != "":
            installSteamcmd(values['-STEAMCMD_INSTALL_FOLDER-'])
            playsound('beep.mp3')
            sg.popup('SteamCMD has been downloaded and installed to ' + values['-STEAMCMD_INSTALL_FOLDER-'])
        else:
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
            sg.popup('Please select an install directory for SteamCMD')
            
window.close()
