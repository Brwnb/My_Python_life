#031Exercicio.py
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# calcule o preço da passagem, cobrando R$0,50 por km para viagens
# de até 200Km e R$0,45 para viagens mais longas.

value = float(input("Enter the distance: "))
if value <= 200 and value > 0:
	print("The value is {:.2f}".format(value*0.50))
elif value > 200:
	print("The value is {:.2f}".format(value*0.45))
