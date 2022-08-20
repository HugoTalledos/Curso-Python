def run():
	counter = 0
	with open('NombreDelArchivo') as f:				#Si no existe el archivo lo crea, si existe lo sobreescribe; w = write
		for line in f:								#with funciona como context manager, sirve para cerrar el archivo 
			counter += line.count('palabra')

	print('Palabra buscada en el archivo aparece {} veces'.format(counter))
			

if __name__ == '__main__':
	run()


#open recibe otro parametro que es la accion con el archivo
# w = write
# r = read
# f es una lista en el que cada elemento es un renglon del archivo