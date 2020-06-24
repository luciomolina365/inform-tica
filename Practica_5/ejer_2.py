import PySimpleGUI as sg 
import json


def leerArchivo():
    try:
        with open('juegadores_ejer_2_p4.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('juegadores_ejer_2_p4.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('juegadores_ejer_2_p4.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(values):

    datos = leerArchivo()
    
    datos[len(datos)] = values         

    escribirArchivo(datos)

def añadir_o_modificar(values):
    
    datos= leerArchivo()
    nombre = str(values["__nombre__"]).lower()

    datos[nombre] = {"Nivel": values["__nivel__"] , "PuntajeMAX": values["__puntajeMAX__"] , "Tiempo":values["__tiempo__"] + " horas"  }
        
    escribirArchivo(datos)




layout = [
    
    [sg.Text("Nombre") , sg.InputText(key="__nombre__")],
    [sg.Text("Nivel") , sg.InputText(key= "__nivel__")],
    [sg.Text("PuntajeMAX") , sg.InputText(key= "__puntajeMAX__")],
    [sg.Text("Tiempo") , sg.InputText(key= "__tiempo__")],
    [sg.Button("Añadir", key="__añadir__")],
    [sg.Exit()]

]


window = sg.Window("Ejercicio 2" , layout, finalize=True)


while True:
    event, values = window.read()
    print(event, values)

    if event in (sg.WIN_CLOSED, "Exit"):
        break
    
    elif event == "__añadir__":
        añadir_o_modificar(values)
        