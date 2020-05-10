import json

def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('verbos.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('verbos.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open('verbos.json' , 'w') as archivo:
        json.dump(datos,archivo)


def cargarDatos(values):

    jugadores = leerArchivo()
    
    nombre = str(values['_nombre_']).lower()
    jugadores[nombre] = {
        'puntaje': int(values['_puntajemax_']),
        'nivel': int(values['_nivel_']),
        'tiempo': int(values['_tiempo_'])
    }

    escribirArchivo(jugadores)