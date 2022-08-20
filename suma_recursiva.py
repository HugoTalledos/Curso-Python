def run():
	number1 = int(input('ingresa un numero: '))
	number2 = int(input('ingresa segundo numero: '))

	print ("resultado de suma:  {}".format(sum(number1)))

def sum(num1):
	if num1 == 1:
		return 1
	return num1 + sum(num1-1)



if __name__ == '__main__':
	run()