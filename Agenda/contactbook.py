from contact import Contact
import csv

class Contactbook:

	def __init__(self):
			self._contacts=[]	#variable privada '_variable'

	def add(self, name, phone, email):
		contact = Contact(name, phone, email)
		self._contacts.append(contact)
		self._save()

	def show_all(self):
		for contact in self._contacts:
			self._print_contact(contact)	#metodo privado 

	def delete (self, name):
		for indx, contact in enumerate(self._contacts):
			if contact.name.lower() == name.lower():
				del self._contacts[indx]
				self._save()
				break

	def search(self, name):
		for contact in self._contacts:
			if contact.name.lower() == name.lower():
				self._print_contact(contact)
				break
		else:
			self._not_found(name)

	def update_contact(self, name, new_name, new_phone, new_email):
		for contact in self._contacts:
			if contact.name.lower() == name.lower():
				contact.name = new_name
				contact.phone = new_phone
				contact.email = new_email
				self._save()
				break
		else:
			self._not_found(name)

	def _save(self):
		with open('contacts.csv', 'w', newline = '') as f:
			writer = csv.writer(f)
			writer.writerow( ('name', 'phone', 'email') )

			for contact in self._contacts:
				writer.writerow( (contact.name, contact.phone, contact.email) )

	def _not_found(self, name):
		print('---*---*---')
		print('Contacto {} no encontrado'.format(name))
		print('---*---*---')


	def _print_contact(self,contact):		#Así se define un metodo privado
		print('---*---*---*---*---*---*---*---')
		print('Nombre: {}'.format(contact.name))
		print('Teléfono: {}'.format(contact.phone))
		print('Email: {}'.format(contact.email))
		print('---*---*---*---*---*---*---*---')

