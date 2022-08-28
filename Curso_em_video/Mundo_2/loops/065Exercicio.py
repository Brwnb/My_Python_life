#065Exercicio.py
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

plus = maior = menor =count = value = 0

exit = 'N'
while exit != "S":
	value = int(input("Enter with a value: "))
	plus += value
	count += 1
	exit = input("If you want exit typed [S]").upper()
	if count == 1:
		maior = menor = value 
	else:
		if value > maior:
			maior = value
		if value < menor:
			menor = value

print("the AVG is {}".format(plus/count))
print('O Maior valor foi {} e o menor foi {}'.format(maior, menor))