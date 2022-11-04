import PySimpleGUI as sg
sg.theme('DarkAmber')

mainMenuLayout = [  
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