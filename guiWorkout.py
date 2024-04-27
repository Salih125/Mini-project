import PySimpleGUI as sg


<<<<<<< HEAD
# Create the Window
window = sg.Window('Workout', layout)
=======
def popup_workout():
    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
>>>>>>> fd5f8b6028e8d418c4ec8501f05ec4de6e8b3ca5

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()