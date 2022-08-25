#039Exercicio.py
#Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade: 
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o tempo que falta 
# ou que passou do prazo.

age = int(input("Enter with the your birth year: "))

if age == 18:
	print("Time to enlist")
elif age < 18:
	print("You don't have to enlist yet")
	print("Still {} yars to enlist".format(18 - age))
else:
	print("You are so old that you don't need to enlist anymore" )
	print("You enlist spent {} years".format(age - 18))
	