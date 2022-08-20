calificaciones = {}

calificaciones['algoritmos'] = 9
calificaciones['web'] = 10
calificaciones['Bases'] = 7
calificaciones['matematicas'] = 8

for key in calificaciones:
	print(key) 		#Imprime las llaves del diciionario

for value in calificaciones.values():
	print(value)	#Imprime los valores del diccionario / no orden

for key, value in calificaciones.items():
		print('llave: {}, valor: {}'.format(key,value))