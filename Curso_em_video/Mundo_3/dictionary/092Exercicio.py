#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e 
#carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
#além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dicionario = dict()
lista = list()

while True:
	dicionario['nome'] = input("Entre com o nome: ")
	dicionario['AnoNascimento'] = int(input("Entre com ano de nascimento: "))
	dicionario['CTPS'] = int(input("Entre com o numero da carteira de trabalho: "))
	if dicionario['CTPS'] != 0:
		dicionario['AnoContratacao'] = int(input("Entre com o ano de contratação: "))
		dicionario['salario'] = float(input("Entre o salário: "))
		dicionario['aposentar'] = ((dicionario['AnoContratacao'] + 35) - datetime.now().year)
		dicionario['idade'] = (datetime.now().year - dicionario['AnoNascimento'])
	
	lista.append(dicionario.copy())
	parar = input("Quer parar? digite [S/s] para parar: ")
	if parar in 'Ss':
		break

for i in lista:
	for k, v in i.items():
		print(f'{k} tem o valor {v}')	 
