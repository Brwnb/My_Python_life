#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias 
#pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres 
#D) Uma lista de pessoas com idade acima da média

pessoas = dict()
lista = list()
soma = 0
while True:
	pessoas['nome'] = input("Digite o nome: ")
	pessoas['sexo'] = input("Digite o sexo: ")
	pessoas['idade'] = int(input("Digite a Idade: "))
	lista.append(pessoas.copy())
	stop = input("Deseja Parar? digite [S/s] ")
	if stop in 'Ss':
		break



print(f"A quantidade de pessoas cadastradas é {len(lista)}")
for i in lista:
	soma += i["idade"]
media = soma/len(lista)
print(f'A media das idades é {media:.2f}')


print('As mulheres cadastradas foram: ', end='')
for i in lista:
	if i['sexo'] in 'Ff':
		print(f'{i["nome"]}', end=" ")
print()

print("Lista das pessoas que estão acima da média ")
for i in lista:
	if i['idade'] > media:
		for k, v in i.items():
			print(f'{k} = {v} ', end='')
		print()
print()
