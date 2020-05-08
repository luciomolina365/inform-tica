
import PySimpleGUI as sg
import json

# Funciones que nos ayudan a la resolucion del ejercicio
def leerArchivoJugadores():
    dic_jugadores = {}
    # Tarea: Pensar como manejar exceptions aca
    with open('ejer_5_jugadores.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos

def escribirArchivoJugadores(jugadores):
    with open('ejer_5_jugadores.json', 'w') as archivo:
        json.dump(jugadores,archivo)

def cargarJugador(values):
    jugadores = leerArchivoJugadores()
    #sg.Print(jugadores)

    nombre = str(values['_nombre_']).lower()

    if nombre in jugadores.keys():
        if int(values['_puntaje_']) > jugadores[nombre]['puntaje']:
            jugadores[nombre] = {
                'puntaje': int(values['_puntaje_']),
                'nivel': int(values['_nivel_']),
                'tiempo': int(values['_tiempo_'])
            }
        # for key,value in jugadores[nombre].items():
        #     if jugadores[nombre][key] == values['_'key]

    else:
        jugadores[nombre] = {
                'puntaje': int(values['_puntaje_']),
                'nivel': int(values['_nivel_']),
                'tiempo': int(values['_tiempo_'])
            }

    # jugadores[nombre] = {
    #     'puntaje': int(values['_puntaje_'])
    #     'nivel': int(values['_nivel_'])
    #     'tiempo': int(values['_tiempo_'])
    # }

    escribirArchivoJugadores(jugadores)


# Definir el layout
layout = [
    [sg.Text('Nombre'),sg.Input(key='_nombre_')],
    [sg.Text('Puntaje'),sg.Input(key='_puntaje_')],
    [sg.Text('Nivel'),sg.Input(key='_nivel_')],
    [sg.Text('Tiempo'),sg.Input(key='_tiempo_')],
    [sg.Button('cargar'), sg.Exit()]
]

window = sg.Window('Ejercicio 5').Layout(layout).Finalize() 

# Loop para capturar los eventos de window
while True:
    event, values = window.Read()

    # sg.Print(event)
    # sg.Print(values)

    #window.FindElement()

    if event is None or event == 'Exit':      
        break
    elif event == 'cargar':
        if values['_nombre_'] == '' or values['_puntaje_'] == '' or values['_nivel_'] == '' or values['_tiempo_'] == '':
            sg.Popup('Falta completar algun campo')
        else:
            cargarJugador(values)


