#080Exercicio.py
#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta de inserção 
#(sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(5):
	value = (int(input("Digite um valor: ")))
	if i == 0 or value > lista[-1]:
		lista.append(value)
	else:
		pos = 0
		while pos < len(lista):
			if value <= lista[pos]:
				lista.insert(pos, value)
				break
			pos += 1

print(lista)
