#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

pessoas = []
lista =[]
maior = menor = 0
aux = 0
while True:
	pessoas.append(input('Nome: '))
	pessoas.append(int(input('Peso: ')))
	lista.append(pessoas[:])
	pessoas.clear()
	stop = input("Para parar digite 'N': ")
	if stop in 'Nn':
		break

print(f'Foram cadastradas {len(lista)} pessoas')

for p in lista:
	if aux == 0:
		maior = menor = p[1]
	else:
		if p[1] > maior:
			maior = p[1]
		if p[1] < menor:
			menor = p[1]
	aux += 1

print(f'O maior peso foi {maior} das pessoas ', end='')
for c in lista:
	if c[1] == maior:
		print(f'{c[0]}', end='')
print()
print(f'O menor peso foi {menor} das pessoas ', end='')
for c in lista:
	if c[1] == menor:
		print(f'{c[0]}', end='')
print()
