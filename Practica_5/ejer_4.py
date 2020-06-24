import PySimpleGUI as sg
import json

def armar_tupla(cadena):
    cadena=cadena.replace("(", "").replace(")", "")
    cadena = cadena.split(",")

    tupla = (int(cadena[0]) , int(cadena[1]))

    return tupla

def sacar_info(direccion):
    
    f = open(direccion,"r")
    aux = f.readlines()
    f.close()

    datos = []

    if "(" in aux[0]:

        for cadena in aux:
            datos.append(armar_tupla(cadena))
    
    else:

        for color in aux:
            datos.append(color.replace("\n" , ""))

    return datos

def armar_dic(lista_colores,lista_coordenadas):
    dic = {}

    for i in range(len(lista_colores)):
        dic[lista_coordenadas[i]] = lista_colores[i]

    print(dic)    
    return dic

#=========================================================================================================================================================

layout = [
    [sg.Input(visible=False, enable_events=True, key="_file1_"), sg.FilesBrowse("Elegir archivo de coordenadas")],
    [sg.Input(visible=False, enable_events=True, key="_file2_"), sg.FilesBrowse("Elegir archivo de colores")],
    [sg.Exit()]
        ]

window = sg.Window('MODICAR DATOS DE JUGADOR').Layout(layout).Finalize()

while True:
    event, values = window.Read()

    if event is None or event == 'Exit':      
        break

    elif event == "_file1_":

        lista1 = sacar_info(values["_file1_"])
        print(lista1)
        print("-.,-,."*25)
        lista_coordenadas = lista1[:]

    elif event == "_file2_":

        lista2 = sacar_info(values["_file2_"])
        print(lista2)
        print("-.,-,."*25)
        lista_colores = lista2[:]

window.Close()

#=========================================================================================================================================================

dic = armar_dic(lista_colores,lista_coordenadas)

#=========================================================================================================================================================

layout =[[sg.Graph(canvas_size=(666, 666), graph_bottom_left=(0, 0), graph_top_right=(666, 666), background_color='red', enable_events=True, key='graph')],
        [sg.Button("Marcar puntos")]
        ]

window = sg.Window('Graph test', layout, finalize=True)

graph = window['graph']        


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Marcar puntos":
        for coor in dic.keys():
            graph.draw_point( coor , size=50 , color = str(dic[coor]))
window.close()