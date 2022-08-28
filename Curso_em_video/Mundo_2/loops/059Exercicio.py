#059Exercicio.py
#Crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar, 2 multiplicar,3 maior valor, 4 novos números e 5 sair do programa.

run = True
while run:
	print("+++Menu++++")
	print("1 soma")
	print("2 Multiplica")
	print("3 escolher o maior valor")
	print("4 novos números")
	print("5 sair")
	value = input("Escolha um valor acima: ")
	if value == '1':
		num1 = int(input('Digite um valor: '))
		num2 = int(input('Digite outro valor: '))
		print("O valor da Soma é: {}".format(num1 + num2))
	elif value == '2':
		num1 = int(input('Digite um valor: '))
		num2 = int(input('Digite outro valor: '))
		print("O valor da multiplicação é: {}".format(num1 * num2))
	elif value == '3':
		num1 = int(input('Digite um valor: '))
		num2 = int(input('Digite outro valor: '))
		if num1 > num2:
			print("O maior valor é {}".format(num1))
		else:
			print("O maior valor é {}".format(num2))
	elif value == '4':
		num1 = int(input('Digite um valor: '))
		num2 = int(input('Digite outro valor: '))
	elif value == '5':
		run = False
		print("Thanks to used the program!!!")


