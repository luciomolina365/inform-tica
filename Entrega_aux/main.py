import PySimpleGUI as sg
import json

#==========================================================================
def modificar(values):
    
    jugadores = leerArchivo()
    nombre = str(values['_nombre_']).lower()
 
    
    jugadores[nombre] = {
        "apellido" : str(values["_apellido_"]),
        "Juegos": "NONE",
    }

    escribirArchivo(jugadores)


def ventanaEleccionJuego():
    
    layout = [
    [sg.Button("Ahorcado" , key='_ahorcado_') , sg.Button('TaTeTi' , key='_tateti_') , sg.Button('Reverse', key='_reverse_')],        
    [sg.Exit()]
    ]

    window = sg.Window('JUEGOS').Layout(layout).Finalize()

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
    if values['_nombre_'] == '' or values['_apellido_'] == '':
        return True
    else:
        return False


def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('jugadores.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('jugadores.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('jugadores.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(values):

    jugadores = leerArchivo()
    
    
    jugadores[len(jugadores)] = {
        "nombre" : str(values['_nombre_']).lower(),   
        "apellido" : str(values["_apellido_"]).lower(),
        'Juegos': "NONE"
    }

    escribirArchivo(jugadores)
#--------------------------------------------------------------------------




#PROGRAMA PRINCIPAL

#Definimos la ventana
layout = [
    [sg.Text("Nombre") , sg.Input(key='_nombre_')],
    [sg.Text("Apellido") , sg.Input(key='_apellido_')],     
    [sg.Button('Elegir juego') , sg.Exit()]
]

window = sg.Window('Ingrese sus datos').Layout(layout).Finalize() 
# Loop para capturar los eventos de window

while True:
    event, values = window.Read()
    
    if event is None or event == 'Exit':      
        break

    elif event == 'Elegir juego':
        
        if faltaCompletar(values):                  
            sg.Popup('Falta completar algun campo') 
        else:         
            cargarDatos(values)
            #VENTANA DE ELECCION DE JUEGO
            #window.Close()

ventanaEleccionJuego()