#Exercício Python 077: Crie um programa que tenha uma tupla com várias 
#palavras (não usar acentos). Depois disso, você deve mostrar, 
#para cada palavra, quais são as suas vogais.

tupla = ('Maça', 'Laranja', 'Pera', 'Mamao')

for i in tupla:
	print(i, end=" || ")
	for j in i:
		if j in 'aeiou':
			print(j, end=" ")
		
	print()
