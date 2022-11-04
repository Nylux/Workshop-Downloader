import PySimpleGUI as sg
sg.theme('DarkAmber')

steamcmdMenuLayout = [
                        [sg.Text('Pick folder where steamcmd should be installed :')],
                        [sg.Input(), sg.FolderBrowse(key="-STEAMCMD_INSTALL_FOLDER-")],
                        [sg.Column([
                            [sg.Button('Back'), sg.Button('DOWNLOAD', key='-DOWNLOAD_STEAMCMD-')],
                        ], justification='center')
                        ]
                     ]