#Exercício Python 083: Crie um programa onde o usuário digite uma expressão Matemática
#qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão 
#passada está com os parênteses abertos e fechados na ordem correta.

#frase = input("Digite um valor: ")
#if frase[0] == '(' and frase[-1] == ')':
#	print(f"A frase {frase} está correta")
#else:
#	print("Tente de novo")

expressao = input("Entre com uma expressao matematica: ")

count1 = 0
count2 = 0
for i in expressao:
	if i == '(':
		count1 += 1
	elif i == ')':
		count2 += 1

if count1 == count2:
	print("A expressão é verdadeira")
else:
	print("A expressão está errada")