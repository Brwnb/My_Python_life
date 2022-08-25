#052Exercicio.py
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

value = int(input("Enter with a value: "))
count = 0
for i in range(1, value + 1):
	if value % i == 0:
		count += 1

if count == 2:
	print("The number is Prime")
else:
	print("The number isn't Prime")