import PySimpleGUI as sg
sg.theme('DarkAmber')

mainMenuLayout = [  
                
                [sg.Column([
                    [sg.Button('Install SteamCMD', key='-STEAMCMD-', tooltip='Click to install SteamCMD if you dont have it already')],	
                ], justification='center'),],
                [sg.HorizontalSeparator(pad=(0, 10))],
                [sg.Text('Pick steamcmd install folder :')],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Text('Pick output folder :')],
                [sg.Input(), sg.FolderBrowse()],
                [sg.HorizontalSeparator(pad=(0, 10))],
                [sg.Column([
                    [sg.Button(button_text='Exit'), 
                    sg.Button(button_text='Next', bind_return_key=True)]
                    ], justification='center')]
                ]