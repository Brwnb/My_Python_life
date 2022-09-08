#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
#que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(vector):
	maior = 0
	print(f'Números digitados')
	for i in range(len(vector)):
		print(vector[i], end=' ')
		if i == 0:
			maior = vector[i]
		else:
			if maior < vector[i]:
				maior = vector[i]
	print()
	print(f'O maior valor é {maior}')




vetor = []
while True:
	vetor.append(int(input("Entre com o valor: ")))
	verifica = input("Para parar digite [N/n]: ")
	if verifica in 'Nn':
		break

maior(vetor)
