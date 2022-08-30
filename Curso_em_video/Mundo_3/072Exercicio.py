#072Exercicio.py
#Exercício Python 72: Crie um programa que tenha uma 
#tupla totalmente preenchida com uma contagem por 
#extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por 
#extenso

tuple_made = ('zero','um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
	'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoite', 'dezenove', 'vinte')


while True:
	value = int(input("Entre com um valor entre entre 0 e 20: "))
	if value >= 0 and value <= 20:
		print(f"O número escolhido é {tuple_made[value]}")
		break
	else:
		value = int(input("Entre com um valor entre entre 0 e 20:  "))
