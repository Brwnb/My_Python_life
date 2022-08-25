#038Exercicio.py
# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem: 
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.
#

value1 = int(input("Enter with the first value: "))
value2 = int(input("Enter with the second value: "))

if value1 < value2:
	print("The number {} is minor than {}".format(value1, value2))
elif value1 > value2:
	print("The number {} is major than {}".format(value1, value2))
else:
	print("They are iquals")