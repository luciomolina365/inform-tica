import PySimpleGUI as sg
import json

import hangman
import reversegam
import tictactoe

#========================METODOS DE LA VENTANA DE ELECCION DE JUEGO==================================================
def modificar(jugador,event):
    
    jugadores = leerArchivo()
    nombre = str(jugador).lower()
    
    if jugadores[nombre]["Juegos"] == "":
        jugadores[nombre]["Juegos"] = event
    
    
    else:
        listaJuegos = jugadores[nombre]["Juegos"].split(",")
        
        if event not in listaJuegos:
            jugadores[nombre]["Juegos"] = jugadores[nombre]["Juegos"] + "," + event 
        
    escribirArchivo(jugadores)


def ventanaEleccionJuego(jugador):
    
    layout = [
    [sg.Button("Ahorcado") , sg.Button("TaTeTi") , sg.Button("Reverse")],        
    [sg.Exit()]
    ]

    window = sg.Window('JUEGOS').Layout(layout).Finalize()
    
    while True:
        event, values= window.Read()  #QUISE USAR KEYS PARA NO TENER QUE PASAR "event" A "MODIFICAR()", PERO EL PROGRAMA SE TRABA 

        if event is None or event == 'Exit':      
            break

        elif event == "Ahorcado":
            modificar(jugador,event)
            window.Close()
            hangman.main()                 
            break
        
        elif event == "TaTeTi":
            modificar(jugador,event)
            window.Close()
            tictactoe.main()          
            break
        
        elif event == "Reverse":
            modificar(jugador,event)
            window.Close()
            reversegam.main()            
            break
#====================================================================================================================
  



#-----------------------METODOS GENERALES----------------------------------------------------------------------------
def faltaCompletar(values):
    if values['_nombre_'] == '':
        return True
    else:
        return False


def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca. EDIT: LISTO!
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

    datos = leerArchivo()
    
    nombre = str(values['_nombre_']).lower()

    if nombre not  in datos.keys(): 
        datos[nombre] = {   
        'Juegos': ""
        }        

    escribirArchivo(datos)
#--------------------------------------------------------------------------------------------------------------------




#PROGRAMA PRINCIPAL

#Definimos la ventana
layout = [
    [sg.Text("Nombre") , sg.Input(key='_nombre_')],    
    [sg.Button('Elegir juego') , sg.Exit()]
]

window = sg.Window('Ingrese sus datos').Layout(layout).Finalize() 
# Loop para capturar los eventos de window

while True:
    event,values = window.Read()
    
    if event is None or event == 'Exit':      
        break

    elif event == 'Elegir juego':
        
        if faltaCompletar(values):                  
            sg.Popup('Falta completar algun campo') 
        else:         
            cargarDatos(values)
            window.Close()
            ventanaEleccionJuego(values["_nombre_"])
            break            

            
