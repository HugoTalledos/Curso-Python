def average_temps(temps):
	sum_of_temps = 0

	for temp in temps: #recorre la lista de temperaturas
		sum_of_temps+=temp
	return sum_of_temps / len(temps)


if __name__ == '__main__':
	temps = [21,23,26,23,22,20,24]

	avarege= average_temps(temps)
	print ('La temperatura promedio: {}'.format(avarege))