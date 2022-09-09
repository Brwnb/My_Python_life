"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de 
forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um 
valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

def leiaint(valor):
	n = str(input(valor))
	if n.isnumeric():
		return 'Tudo Certo'
	else:
		return 'Não é numero não'

n = leiaint('Digite um número: ')

print(n)