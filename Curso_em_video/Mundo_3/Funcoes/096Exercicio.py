#Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
#que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

def area(b,a):
	print(f'A are do terreno é {b*a:.2f}.')


base = float(input("Digite o valor da largura: "))
altura = float(input('Digite o valor comprimento: '))

area(base,altura)