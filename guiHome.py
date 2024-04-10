import PySimpleGUI as sg

# Gui theme
sg.theme('DarkTeal12')

layout = [[sg.Text('New Workout: '), sg.Input() ,sg.Button('Add', key = 'addButton'), 
           sg.Button('Remove', key = 'removeButton')],
          [sg.Text('Workouts')],
        [sg.Listbox([1, 2, 3], size=(30, 25), key = 'wList')]
          ]

window = sg.Window('Tracker', layout)

while 1:
    # Reads events and values from elements 
    event, values = window.read()

    #closes the window
    if event == sg.WIN_CLOSED:
        break
            
window.close()