#!/usr/bin/env python
import PySimpleGUI as sg

# Usage of Graph element.

layout = [[sg.Graph(canvas_size=(666, 666), graph_bottom_left=(0, 0), graph_top_right=(666, 666), background_color='red', enable_events=True, key='graph')]]

window = sg.Window('Graph test', layout, finalize=True)

graph = window['graph']        


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'graph':
        graph.draw_point(values['graph'] , size=50 , color= "black")
window.close()