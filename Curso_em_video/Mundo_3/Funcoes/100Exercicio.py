#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções 
#chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
#dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados 
#pela função anterior.

from random import randint


def soma_par(valor):
	soma = 0
	for i in valor:
		if i % 2 == 0:
			soma += i
	print(f'A soma é {soma}')



def sorteia():
	vector = []
	for i in range(5):
		vector.append(randint(-1000,1000))
	print(vector)
	soma_par(vector)



sorteia()