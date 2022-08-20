#-*- coding: utf-8 -*-

#import lamp 	Si se importa una clase así
from lamp import Lamp


def run():
		#lamp = lamp.Lamp(is_turned_on=True)		El objeto se declara así
		lamp = Lamp(is_turned_on=True)			#Instancia de un objeto

		while True: 
			command = str(input(''''
				¿Qué deseas hacer?

				[p]render
				[a]pagar
				[s]alir
				'''))
			if command == 'p':
				lamp.turn_on()					#uso de metodo del objeto
			elif command == 'a':
				lamp.turn_off()
			else:
				break

if __name__ == '__main__':
	run()