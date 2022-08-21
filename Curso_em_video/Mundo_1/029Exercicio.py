# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado.

# A multa vai custar 7,00 por cada km acima do limite

value = int(input("Enter with the value: "))

if value > 80:
	print("Você foi multado")
	print("O valor da multa é {:.2f}".format(7*(value-80)))
