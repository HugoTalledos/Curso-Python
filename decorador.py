
def prueba(func):		#func es la funcion que se recibe por parametro, en este caso protected_func
	def wrapper(password):		#wrapper es la funcion que resive la contraseña 

		if password == '123':
			return func()		#En caso de ser correcto ejecuta protected_func que es la funcion que se recibe como parametro en prueba
		else:
			print("Contraseña incorrecta")

	return wrapper				#Se retorna el objeto 'wrapper' y no la funcion 'wrapper()'


@prueba		#Nombre de la funcion que se ejecuta primero | este es el decorador de la funcion protected_func
def protected_func():
	print('Tu contraseña es correcta.')

if __name__ == '__main__':
	password = str(input('Ingresa tu contraseña: '))

	protected_func(password)