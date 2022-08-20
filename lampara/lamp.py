#-*- coding: utf-8 -*-
#Ejemplo de clase python

class Lamp:
	"""docstring for Lamp"""
	def __init__(self, is_turned_on):							#Constructor, recibe un parametro "is_turned_on"
		self._is_turned_on = is_turned_on

	def turn_on(self):
		self._is_turned_on = True
		self._display_image()

	def turn_off(self):							#Metodo publico
		self._is_turned_on = False
		self._display_image()

	def _display_image(self):					#Metodo privado
			if self._is_turned_on:
				print("La lampara esta prendida")
			else:
				print("La lampara esta apagada")