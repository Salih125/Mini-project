import PySimpleGUI as sg
from exerciseData import ExerciseData

def popup_workout():

    # Instance of ExerciseData class
    e = ExerciseData('')

    # Gui theme
    sg.theme('DarkTeal12')
    
    # Gui Layout
    lst = sg.Listbox(values = ExerciseData.readExercises(), size=(30, 25), key = '-LIST-', enable_events=True)
    
    # All the stuff inside your window.
    layout = [  [sg.Text('Add exercise - name: sets: reps:')],
                [sg.InputText(key = '-EX-')],
                [sg.Button('Add', key = '-ADDBUTTON-'), sg.Button('Remove', key = '-REMOVEBUTTON-')],
                [sg.Text('Exercises: ')],
                [lst] ]

    # Create the Window
    window = sg.Window('Workout', layout)

    exList = e.exercisesList

    # Event Loop to process "events" and get the "values" of the inputs
    while 1:
        # Reads events and values from elements 
        event, values = window.read() 

        #closes the window
        if event == sg.WIN_CLOSED:
            break

         # Adds exercise to list
        if event == '-ADDBUTTON-':
            e.name = values['-EX-']
            e.addExercise(e.name)

            file = open('exercisesFile.txt', 'r')
            contents = file.readlines()
            file.close()
            window['-LIST-'].update(contents)

        # Removes exercise from list
        if event == '-REMOVEBUTTON-':
            file = open('exercisesFile.txt', 'r')
            contents = file.readlines()
            file.close()

            e.name = values['-EX-']
            e.removeExercise(e.name)
            window['-LIST-'].update(contents)

        # if event == '-LIST-':

    window.close()

#popup_workout()