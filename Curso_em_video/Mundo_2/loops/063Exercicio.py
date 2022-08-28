#063Exercicio.py
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
# n primeiros elementos de uma Sequência de Fibonacci.

terms = int(input("Enter with a value: "))
n1, n2 =0, 1
count = 0
while count < terms:
	value = n1 + n2
	n1 = n2
	n2 = value
	count += 1

print(value)
