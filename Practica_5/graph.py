#!/usr/bin/env python
import PySimpleGUI as sg

# Usage of Graph element.

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400), background_color='red', enable_events=True, key='graph')],
          [sg.Button('_DIBUJAR_')]
         ]

window = sg.Window('Graph test', layout, finalize=True)

graph = window['graph']         # type: sg.Graph


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == '_DIBUJAR_':
        graph.draw_point((0,0) , size=50 , color= "black" )
window.close()