"""Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na 
tela o processo de cálculo do fatorial.
"""
def fatorial(value):
	fatorial = 1
	while value > 1:
		fatorial = fatorial * value
		value -= 1

	return fatorial

fator = fatorial(int(input("Digite um numero: ")))
print(f'O fatorial do número é: {fator}')
