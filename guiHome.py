import PySimpleGUI as sg
from workoutData import WorkoutData
import guiWorkout
import guiCalculator

# Instance of WorkoutData class
w = WorkoutData('')

# Gui theme
sg.theme('DarkTeal12')

# Gui Layout
lst = sg.Listbox(values = WorkoutData.readWorkouts(), size=(30, 25), key = '-LIST-', enable_events=True)

layout = [[sg.Text('New Workout: '), sg.Input(key = '-INPUT-'), sg.Button('Add', key = '-ADDBUTTON-'), 
           sg.Button('Remove', key = '-REMOVEBUTTON-')],
          [sg.Text('Workouts')],
        [lst],
        [sg.Button('Calculator', key = '-CALC-')]
          ]

# Creates window
window = sg.Window('Tracker', layout)

lists = w.workouts

while 1:
    # Reads events and values from elements 
    event, values = window.read()

    #closes the window
    if event == sg.WIN_CLOSED:
        break
    
    # Adds workout to list
    if event == '-ADDBUTTON-':
        w.name = values['-INPUT-']
        w.addWorkout(w.name)
        
        file = open('workoutsFile.txt', 'r')
        contents = file.readlines()
        file.close()
        window['-LIST-'].update(contents)
        
    # Removes workout from list
    if event == '-REMOVEBUTTON-':
        file = open('workoutsFile.txt', 'r')
        contents = file.readlines()
        file.close()

        w.name = values['-INPUT-']
        w.removeWorkout(w.name)
        window['-LIST-'].update(contents)

    # Opens guiWorkout when clicked at a workout
    if event == '-LIST-':
        guiWorkout.popup_workout()

    if event == '-CALC-':
        guiCalculator.popup_calc()

window.close()