import PySimpleGUI as sg
import json


layout = [
    [sg.Input(visible=False, enable_events=True, key="_file_"), sg.FilesBrowse()],
    [sg.Exit()]
        ]



window = sg.Window('MODICAR DATOS DE JUGADOR').Layout(layout).Finalize()

while True:
    event, values = window.Read()

    if event is None or event == 'Exit':      
        break

    if event == "_file_":
        print(event)
        print(values)

window.Close()





#archivo = open(values["_file_"] , "r")

#print(archivo.read())



