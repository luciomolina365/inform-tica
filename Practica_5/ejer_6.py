import  PySimpleGUI as sg 
import json

def leerArchivo():
    try:
        with open('jason_de_ejer_6.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('jason_de_ejer_6.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('jason_de_ejer_6.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(values):

    datos = leerArchivo()

    print(values)

    datos[len(datos)] = values         

    escribirArchivo(datos)



colores = ["yellow","blue","green","black"]

layout =[
        [sg.InputCombo(values = colores , default_value = colores[0] , key = "__inputCombo__")],
        
        [sg.Frame('Coordenadas X , Y',[
        [sg.Slider(range=(0, 666), orientation='v', size=(13, 25), default_value=0,key="__x__"),
        sg.Slider(range=(0, 666), orientation='v', size=(13, 25), default_value=0,key="__y__")]]), 
        sg.Listbox([], size = (90,16) , key = "__listBox__" , select_mode=True)],

        [sg.Button("Añadir")],
        [sg.Button("Guardar") , sg.Exit()]
        ]

window = sg.Window('Ejercicio_6', layout, finalize=True)


listaDeBox = [] 

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED , "Exit"):
        break
    elif event == "Añadir":
        listaDeBox.append( {"Coordenadas":(int(values["__x__"]),int(values["__y__"])) , "Color":values["__inputCombo__"]} )
        window["__listBox__"].update(listaDeBox)
    elif event == "Guardar":
        datos = values["__listBox__"][0]
        cargarDatos(datos)
window.close()