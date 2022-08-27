#057Exercicio.py
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F"
#Caso esteja errado, peça a digitação novamente do valor correto.

run = True
while run:
	sex = input("Enter with the sex (use F or M): ").upper()
	if sex == 'M' or sex == 'F':
		run = False
	else :
		print("Enter with the corrected word!!")
		print("Use F or M")
		run = True

