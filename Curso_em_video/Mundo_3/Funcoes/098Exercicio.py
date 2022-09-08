#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
#que receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
#três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
#c) uma contagem personalizada 

from time import sleep

def contador(inicio, fim, passo):

	for i in range(inicio,fim+1,passo):
		print(i, end=' ', flush=True)
		sleep(0.3)
	print()



contador(1,10,1)
contador(10,0,-2)
a = int(input("Digite o valor inicial: "))
b = int(input("Digite o valor final: "))
c = int(input("Digite o valor do passo: "))
contador(a,b,c)
