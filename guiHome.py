import PySimpleGUI as sg

sg.theme('DarkTeal12')
layout = [[sg.Text('Text test')], 
        [sg.Text('Enter something '), sg.InputText()]
          ]

window = sg.Window('Tracker', layout)

while 1:
    event, values = window.read()

window.close()