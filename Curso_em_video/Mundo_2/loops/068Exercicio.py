#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de 
#vitórias consecutivas que ele conquistou no final do jogo. 

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
