import pickle
import time


def leo():
	
	archivo = open("datosRepasoPICKLE.txt", "rb")
	datos = pickle.load(archivo)
	for item in datos:
			for item, valor in item.items():
					print("{}: {}".format(item, valor))
	archivo.close()

def grabo():

	# archivo = open("datosRepasoPICKLE.txt", "rb")

	# datos = pickle.load(archivo)
	# archivo.close()
	archivo = open("datosRepasoPICKLE.txt", "wb")

	datos = []
	print('Ingresa tu nombre')
	nom = input()
	while nom != 'zz':
		datos.append({'nombre': nom,'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())})

		print('Ingresa tu nombre')
		nom = input()

	pickle.dump(datos, archivo)
	#otro.close()
	archivo.close()
	

if __name__ == '__main__':

	grabo()
	leo()
