from contactbook import Contactbook
import csv

def run():
	
	contact_book = Contactbook()

	try:
		with open('contacts.csv', 'r') as f:
			reader = csv.reader(f)
			for idx, row in enumerate(reader):
				if idx == 0:
					continue

			contact_book.add(row[0], row[1], row[2])
	except FileNotFoundError as e:
		print('Agenda nueva')

	while True:
			command = str(input('''
				¿Qué deseas hacer?

				[a]ñadir contacto
				[ac]tualizar contacto
				[b]uscar contacto
				[e]liminar contacto
				[l]istar contactos
				[s]alir
			'''))

			if command == 'a':

				name = str(input('Nombre de contacto: '))
				phone = str(input('Telefono de contacto: '))
				email = str(input('Email de contacto: '))
				contact_book.add(name, phone, email)

			elif command == 'ac':
				
				name = str(input('¿Qué contacto quieres actualizar? '))
				contact_book.search(name)

				new_name = str(input('Nuevo nombre: '))
				new_phone = str(input('Nuevo teléfono: '))
				new_email = str(input('Nuevo email: '))

				contact_book.update_contact(name, new_name, new_phone, new_email)

			elif command == 'b':
				
				name = str(input('¿Qué contacto quieres buscar? '))
				contact_book.search(name)

			elif command == 'e':

				name = str(input('¿Qué contacto quieres eliminar? '))
				contact_book.delete(name)

			elif command == 'l':

				contact_book.show_all()

			elif command == 's':
				break;
			else:
				print('Comando no encontrado.')

if __name__ == '__main__':
	print(' B I E N V E N I D O A LA A G E N D A ')
	run()
