#028Exercicio
#Escreva um programa que faça o computador pensar em um
#número inteiro entre 0 e 5 e peça para o computador
#o usuário tentar desobrir qual foi o número escolhido pelo
#computaodr
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

value = randint(0,5)
num = int(input("Enter with a number between 0 and 5: "))

if value == num:
	print("O usuário venceu")
else:
	print("O usuário perdeu")
