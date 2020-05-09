import PySimpleGUI as sg
import time
import json

#--------------------------------------------------------------------------


def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('ejer_1_clima.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos
    
    except FileNotFoundError:
        with open('ejer_1_clima.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(clima):
    with open('ejer_1_clima.json' , 'w') as archivo:
        json.dump(clima,archivo)



def cargarJugador(lista):

    datos=leerArchivo()

    datos[len(datos)] = {
        "Temperatura": lista[0],
        "Humedad": lista[1],
        "Fecha": lista[2]
    }

    escribirArchivo(datos)


#--------------------------------------------------------------------------



layout = [
    [sg.Text("Temperatura") , sg.Input(key='_temperatura_')],
    [sg.Text('Humedad'),sg.Input(key='_humedad_')],    
    [sg.Button('Añadir')],
    [sg.Button('Guardar en json'), sg.Exit()]
]


window = sg.Window('Ejercicio 1').Layout(layout).Finalize() 
# Loop para capturar los eventos de window
while True:
    event, values = window.Read()
    

    if event is None or event == 'Exit':      
        break

    elif event == 'Añadir':
        
        if values['_temperatura_'] == '' or values['_humedad_'] == '':
            sg.Popup('Falta completar algun campo')                   
            
        else:         
            fecha= time.strftime("%d %b %Y , %H:%M", time.localtime())
            lista = [str(values['_temperatura_']) + " grados" , str(values['_humedad_']) + "%" , fecha]
    
    elif event == "Guardar en json":
        try:cargarJugador(lista)
        except NameError:
            sg.Popup('Falta añadir los datos')