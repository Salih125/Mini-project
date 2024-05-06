import PySimpleGUI as sg
from nutritioncalculator import Nutritioncalculator as nc

def popup_calc():
    cal = 0
    pro = 0
    weight = 0

    # Gui theme
    sg.theme('DarkTeal12')

    # All the stuff inside your window.
    layout = [  [sg.Text('Protein:')],
                [sg.Text('Weight: '), sg.InputText(key = '-PROW-'), sg.Button('Calculate', key = '-PROCALC-')],
                [sg.Text('Proteins: '), sg.Text(pro, key = '-PRORES-'), sg.Text('grams')],
                [sg.Text('Calories:')],
                [sg.Text('m/f')],
                [sg.InputText(key = '-GENDER-')],
                [sg.Text('Weight')],
                [sg.InputText(key = '-WEIGHT-')],
                [sg.Text('Height')],
                [sg.InputText(key = '-HEIGHT-')],
                [sg.Text('Age')],
                [sg.InputText(key = '-AGE-'), sg.Button('Calculate', key = '-CALCALC-')],
                [sg.Text('Calories: '), sg.Text(cal, key = '-CALRES-')]]
    
     # Create the Window
    window = sg.Window('Workout', layout)

    while 1:
        # Reads events and values from elements 
        event, values = window.read() 

        #closes the window
        if event == sg.WIN_CLOSED:
            break

        # Calculates proteins 
        if event == '-PROCALC-':
            pro = values['-PROW-']
            res = nc.procalc(float(pro))
            window['-PRORES-'].update(res)

        # Calculates calories
        if event == '-CALCALC-':
            g = values['-GENDER-']
            w = values['-WEIGHT-']
            h = values['-HEIGHT-']
            a = values['-AGE-']
            cal = nc.calcalc(g, float(w), float(h), float(a))
            window['-CALRES-'].update(cal)

    window.close()