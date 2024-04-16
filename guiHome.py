import PySimpleGUI as sg
from workout import Workout

# Instance of Workout class
w = Workout('')

# Gui theme
sg.theme('DarkTeal12')

# Gui Layout
lst = sg.Listbox(values = w.workouts, size=(30, 25), key = '-LIST-')

layout = [[sg.Text('New Workout: '), sg.Input(key = '-INPUT-'), sg.Button('Add', key = '-ADDBUTTON-'), 
           sg.Button('Remove', key = '-REMOVEBUTTON-')],
          [sg.Text('Workouts')],
        [lst]
          ]

# Creates window
window = sg.Window('Tracker', layout)

lists = w.workouts

file = open('workouts.txt', 'r')
contents = file.read()

while 1:
    # Reads events and values from elements 
    event, values = window.read()

    #closes the window
    if event == sg.WIN_CLOSED:
        break
    
    # Adds workout to list
    if event == '-ADDBUTTON-':
        w.name = values['-INPUT-']
        w.createWorkout()
        window['-LIST-'].update(contents)
        
        
    # Removes workout from list
    if event == '-REMOVEBUTTON-':
        val = lst.get()[0]
        w.removeWorkout()
        window['-LIST-'].update(w.workouts)
    

w.workoutsF.close()
window.close()