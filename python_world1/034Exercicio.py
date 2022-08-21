#034Exercicio.py
#Escreva um programa que pergunte ao salário de um funcionário e calcule o valor
# do seu aumento.
# Para salarios superiores a 1250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salary = float(input("Enter with the salary: "))

if salary > 1250.00:
	print("The 10% increase is {:.2f}".format(salary*1.10))
elif salary > 0 and salary <1250.00:
	print("The 15% increase is {:.2f}".format(salary*1.15))
