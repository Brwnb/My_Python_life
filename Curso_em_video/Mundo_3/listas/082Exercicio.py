#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
#ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#from random import randint

lista = list()
#count = 0
impar = list()
par = list()

while True:
#while count <15:
	lista.append(int(input("Entre com um valor: ")))
	resp = input("Quer continuar [S/N]")
	if resp in 'Nn':
		break
	#lista.append(randint(-50, 100))
	#count += 1
for number in lista:
	print(number)
	if number % 2 == 0:
		par.append(number)
		print(number)
	else:
		impar.append(number)
		print(number)
print(f"Lista digitada {lista}")
print(f"Lista com números Pares {par}")
print(f"Lista com números Impares {impar}")