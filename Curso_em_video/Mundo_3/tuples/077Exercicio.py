#Exercício Python 077: Crie um programa que tenha uma tupla com várias 
#palavras (não usar acentos). Depois disso, você deve mostrar, 
#para cada palavra, quais são as suas vogais.

tupla = ('Maça', 'Laranja', 'Pera', 'Mamao')

for i in tupla:
	print(i, end=" || ")
	for j in i:
		if j == 'a':
			print(j, end=" ")
		elif j == 'e':
			print(j, end=" ")
		elif j == 'i':
			print(j, end=" ")
		elif j == 'o':
			print(j, end=" ")
		elif j == 'u':
			print(j, end=" ")
	print()
