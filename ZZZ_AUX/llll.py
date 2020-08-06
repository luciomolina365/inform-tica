import PySimpleGUI as sg
def CreandoTablero(cant):# 
        """Se crea el tablero recibiendo el tablero y la cantidad de filas y columnas,en caso de que sea una partida
        guardada, se cargara las letras en las posiciones donde se formaron palabras correctas"""
        tablero = []
        lista1 = []
        for i in range(cant):
            lista1.clear()
            for j in range(cant):
                    lista1.append(sg.Button( "A",disabled=True,size=(2,1),key=(i,j), pad=(2,3),button_color=('grey','white'), image_filename='', image_size=(25, 22)))

            lista1 = [lista1]
            tablero = tablero + lista1
        return tablero



tablero = CreandoTablero(15)



columna_2 = [ 
 [sg.Text('Tipo Doc'), sg.Listbox(values=('DNI','LE', 'PAS'), size=(30, 1))],
 [sg.Text('Número'), sg.InputText()],
 [sg.Text('Nacionalidad'), sg.InputText()] 
            ]

#Armo el diseño de la interface
diseño = [
 [sg.Text('Ingresa tus datos')],
 [sg.Column(tablero), sg.Column(columna_2)],
 [ sg.Submit(), sg.Cancel()]
]

#La aplico a la ventana y la muestro
window = sg.Window('Datos Personales').Layout(diseño)
window.Read()
