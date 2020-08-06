import PySimpleGUI as sg
import json


def leerArchivo():
    try:
        with open('CLIMA.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('CLIMA.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('CLIMA.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(values):

    datos = leerArchivo()
    
    datos[len(datos)] = values         

    escribirArchivo(datos)



layout = [


    
    [sg.Text("Temperatura") , sg.InputText(key="__temperatura__")],
    [sg.Text("Humedad") , sg.InputText(key= "__humedad__")],
    [sg.Button("Añadir", key="__añadir__") , sg.Button("Guardar", key= "__guardar__")],
    [sg.Exit()]

]

layout2 = [

    [sg.Listbox([], size = (90,10) , key = "__listBox__" , select_mode=True)]

]





columna1 = sg.Column(layout)

columna2 = sg.Column(layout2)

finalas = [columna1 , columna2]

window = sg.Window("Ejercicio 1" , finalas , finalize=True)



lista=[]

while True:
    event, values = window.read()
    print(event, values)


    if event in (sg.WIN_CLOSED, "Exit"):
        break

    elif event == "__añadir__":
        lista.append({"Temperatura" : values["__temperatura__"] + " C " , "Humedad" : values["__humedad__"] + "% " })
        window["__listBox__"].update(lista)

    elif event == "__guardar__":
        datos = values["__listBox__"][0]
        cargarDatos(datos)        