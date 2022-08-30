#Exercício Python 074: 
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e 
#também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = 0
menor = 0
tuplas = (randint(0,50),randint(0,50),randint(0,50),randint(0,50),randint(0,50))

print("Segue os valores da tupla:")
for i in range(len(tuplas)):
	print(f"{tuplas[i]}", end=" ")
print()

menor = tuplas[0]
maior = tuplas[1]
for i in range(len(tuplas)):
	if menor >= tuplas[i]:
		menor = tuplas[i]
	if maior <= tuplas[i]:
		maior = tuplas[i]
print(f"O menor {menor} e o maior {maior}")