#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de 
#vitórias consecutivas que ele conquistou no final do jogo. 
"""
from random import choice
choices = ''
temp = ['PAR','IMPAR']
count = 0
while True:
	choices = input("Choice PAR or IMPAR: ").upper().strip()
	if choice(temp) == choices:
		print("Congrats!! You Won!!")
		count += 1
	else:
		print("Sorry!! You lose!!")
		break
print(f"The loop worked {count} times")
"""

from random import randint
v = 0
while True:
	player = int(input("Enter with  a value between 0 and 5 (one hand okay!!!): "))
	cpu = randint(0 ,5)
	total = cpu + player
	choises = ' '
	while choises not in 'EeOo':
		choises = input("Even or Odd? ").upper().strip()[0]
	print(f'You played {player} and the computer played {cpu}. The Total is {total}')
	print('Came out even' if total % 2 == 0 else 'came out Odd')
	if choises == 'E':
		if total % 2 == 0:
			print("You Won!!!")
			v += 1
		else:
			print("You lose")
			break
	elif choises == 'O':
		if total % 2 == 1:
			print("You Won!!!")
			v += 1
		else:
			print("You lose")
			break
	print("Let's play again")
print(f"Game Over. You won {v} time(s)")