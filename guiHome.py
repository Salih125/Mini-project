import PySimpleGUI as sg

wList = []

# Gui theme
sg.theme('DarkTeal12')

layout = [[sg.Text('New Workout: '), sg.Input(value = input, key = '-WINPUT-') ,sg.Button('Add', key = '-ADDBUTTON-'), 
           sg.Button('Remove', key = '-REMOVEBUTTON-')],
          [sg.Text('Workouts')],
        [sg.Listbox(values = wList, size=(30, 25), key = '-WLIST-')]
          ]

window = sg.Window('Tracker', layout)

while 1:
    # Reads events and values from elements 
    event, values = window.read()

    #closes the window
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-ADDBUTTON-':
        print('addButton pressed')
        wList.append('-WINPUT-')
        window['-WLIST-'].update(wList)
        

    if event == 'removeButton':
        print('removeButton pressed')        
            
window.close()