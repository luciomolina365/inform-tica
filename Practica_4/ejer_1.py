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

def escribirArchivo(datos):
    with open('ejer_1_clima.json' , 'w') as archivo:
        json.dump(datos,archivo)



def cargarDatos(lista):

    datos=leerArchivo()
    
    for elemento in lista:
        
        datos[len(datos)+1]= elemento
    
    lista.clear()
    
    escribirArchivo(datos)
    
#--------------------------------------------------------------------------

#PROGRAMA PRINCIPAL

#Definimos la ventana
layout = [
    [sg.Text("Temperatura") , sg.Input(key='_temperatura_')],
    [sg.Text('Humedad'),sg.Input(key='_humedad_')],    
    [sg.Button('Añadir')],
    [sg.Button('Guardar en json'), sg.Exit()]
]

window = sg.Window('Ejercicio 1').Layout(layout).Finalize() 
# Loop para capturar los eventos de window
lista=[]
while True:
    event, values = window.Read()
    
    if event is None or event == 'Exit':      
        break

    elif event == 'Añadir':
        
        if values['_temperatura_'] == '' or values['_humedad_'] == '':
            sg.Popup('Falta completar algun campo')                   
            
        else:         
            fecha= time.strftime("%d %b %Y , %H:%M", time.localtime())
            aux = {
                "Temperatura": str(values['_temperatura_']) + " grados" , 
                "Humedad": str(values['_humedad_']) + "%" , 
                "Fecha": fecha
            }

            lista.append(aux)
    
    elif event == "Guardar en json":
        try:
            cargarDatos(lista)
        except NameError:
            sg.Popup('Falta añadir los datos')