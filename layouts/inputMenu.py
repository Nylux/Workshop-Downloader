import PySimpleGUI as sg
sg.theme('DarkAmber')

inputMenuLayout = [
                    [sg.Column([
                        [sg.Text('Paste the links of the mods you want to download :')],
                        [sg.Text('WARNING : There should only be one link per line.')],
                        [sg.Text('The app may look frozen, but it is not. Please be patient.')]
                    ], justification='center')],
                    [sg.Multiline(key='-IN-', size=(60, 10))],
                    [sg.HorizontalSeparator(pad=(0, 10))],
                    [sg.Column([
                        [sg.Button(button_text='Back'), 
                        sg.Button(button_text='DOWNLOAD', bind_return_key=True)],
                        ], justification='center')
                    ]
                  ]