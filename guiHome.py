import PySimpleGUI as sg

# Gui theme
sg.theme('DarkTeal12')

wList = []
lst = sg.Listbox(values = wList, size=(30, 25), key = '-WLIST-')

layout = [[sg.Text('New Workout: '), sg.Input(key = '-WINPUT-'), sg.Button('Add', key = '-ADDBUTTON-'), 
           sg.Button('Remove', key = '-REMOVEBUTTON-')],
          [sg.Text('Workouts')],
        [lst]
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
        wList.append(values['-WINPUT-'])
        window['-WLIST-'].update(wList)
        

    if event == '-REMOVEBUTTON-':
        print('removeButton pressed')
        val = lst.get()[0]
        wList.remove(val)
        window['-WLIST-'].update(wList)
                
            
window.close()