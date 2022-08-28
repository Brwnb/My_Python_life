#060Exercicio.py
# Faça um programa que leia um número qualquer e mostre o seu fatorial.

value = int(input("Enter with a number: "))

fatorial = 1
while value > 1:
	fatorial = fatorial * value
	value -= 1

print(fatorial)