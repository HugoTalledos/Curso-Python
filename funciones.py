# -*- codinf: utf-8 -*-

import turtle

def main():			#Funcion principal
	windoe = turtle.Screen()
	figure =  turtle.Turtle()
	make_figure(figure)
	turtle.mainloop()

def make_figure(figure):
	length = int(input('Tamaño de figura '))#Entrada por teclado
	for i in range(4):
		make_line_and_trun(figure, length)

def make_line_and_trun(figure, length):
	figure.forward(length)
	figure.left(90)

if __name__ == '__main__':		#Ejecución de funcíon principal
	main()