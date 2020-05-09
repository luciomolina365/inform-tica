import PySimpleGUI as sg
import json


#==========================================================================
def modificar(values):
    
    jugadores = leerArchivo()
    nombre = str(values['_nombre_']).lower()
 
    if nombre in jugadores.keys():
        jugadores[nombre] = {
        'nivel': int(values['_nivel_']),
        'puntaje': int(values['_puntajemax_']),
        'tiempo': int(values['_tiempo_'])
        }

    escribirArchivo(jugadores)


def modificoDatos():
    
    layout = [
    [sg.Text("Nombre") , sg.Input(key='_nombre_')],
    [sg.Text('Nivel') , sg.Input(key='_nivel_')],    
    [sg.Text('PuntajeMAX') , sg.Input(key='_puntajemax_')],    
    [sg.Text('Tiempo') , sg.Input(key='_tiempo_')],    
    [sg.Button("MODIFICAR") , sg.Exit()]
    ]

    window = sg.Window('MODICAR DATOS DE JUGADOR').Layout(layout).Finalize()
    
    while True:
        event, values = window.Read()
    
        if event is None or event == 'Exit':      
            break
                                          
        elif event == 'MODIFICAR':
            modificar(values)
            if faltaCompletar(values):                  
                sg.Popup('Falta completar algun campo')                              
            else:                      
                modificar(values)
    window.Close()
#==========================================================================
  




#--------------------------------------------------------------------------
def faltaCompletar(values):
    if values['_nombre_'] == '' or values['_nivel_'] == '' or values['_puntajemax_'] == '' or values['_tiempo_'] == '':
        return True
    else:
        return False


def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('ejer_2_jugadores.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('ejer_2_jugadores.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('ejer_2_jugadores.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(lista):

    jugadores = leerArchivo()
    
    for elemento in lista:
        
        nombre=elemento["nombre"]

        del elemento["nombre"]

        jugadores[nombre] = elemento
    
    lista.clear()

    escribirArchivo(jugadores)
#--------------------------------------------------------------------------






#PROGRAMA PRINCIPAL

#Definimos la ventana
layout = [
    [sg.Text("Nombre") , sg.Input(key='_nombre_')],
    [sg.Text('Nivel') , sg.Input(key='_nivel_')],    
    [sg.Text('PuntajeMAX') , sg.Input(key='_puntajemax_')],    
    [sg.Text('Tiempo') , sg.Input(key='_tiempo_')],    
    [sg.Button('Añadir') , sg.Button('Guardar en json')], 
    [sg.Exit()]
]

window = sg.Window('ENTRADA DE DATOS').Layout(layout).Finalize() 
# Loop para capturar los eventos de window
lista=[]
while True:
    event, values = window.Read()
    
    if event is None or event == 'Exit':      
        break
    
    elif event == 'Añadir':
            
        if faltaCompletar(values):
            sg.Popup('Falta completar algun campo')
        else:         
            
            aux= {
                "nombre" : str(values['_nombre_']).lower(),
                'nivel': int(values['_nivel_']),
                'puntaje': int(values['_puntajemax_']),
                'tiempo': int(values['_tiempo_'])
            }
            lista.append(aux)

    elif event == 'Guardar en json':
        try:
            cargarDatos(lista)
        except NameError:
            sg.Popup('Falta añadir los datos')
        
window.Close()

modificoDatos()