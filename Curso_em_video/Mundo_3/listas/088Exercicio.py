#Exercício Python 088: Faça um programa que ajude um 
#jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos 
#jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
#cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = list()
jogos = list()
quant = int(input("Quantos jogos você quer sortear: "))

while quant > 0:
	quant -= 1
	count = 0
	while True:
		valor = randint(1,60)
		if valor not in lista:
			lista.append(valor)
			count += 1
		if count >= 6:
			break
	lista.sort()
	jogos.append(lista[:])
	lista.clear()

print(f'Os numeros soreados são: ')
for i in jogos:
	print(i)
	sleep(1)

