#055Exercicio.py
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o 
#maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(1, 6):
	weigth = float(input("Enter with a weigth: "))
	if i == 1:
		maior = weigth
		menor = weigth
	else:
		if weigth > maior:
			maior = weigth
		if weigth < menor:
			menor = weigth


print("O maior peso lido foi de {} kg" .format(maior))
print("O menor peso lido foi de {} kg" .format(menor))