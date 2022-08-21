#032Exercicio.py
# Faça um programa que leia um ano qualquer e mostre se 
# ele é bissexto

year = int(input("Enter with the year: "))

if year % 4 == 0 and year % 100 != 0:
	print("O número é bissexto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
	print("O número é bissexto Hello")

else:
	print("O número não é bissexto")
