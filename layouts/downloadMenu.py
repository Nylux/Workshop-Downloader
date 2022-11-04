import PySimpleGUI as sg
sg.theme('DarkAmber')

downloadMenuLayout = [
                        [sg.Text('Your mods have been downloaded!')],
                        # [sg.Multiline(key='-OUT-', size=(50, 10), disabled=True)],
                        [sg.Column([
                            [sg.Button(button_text='Exit'), 
                             sg.Button(button_text='Open Output Folder', key='-OUTPUT-')
                             ]
                            ], justification='center')
                        ]
                     ] 