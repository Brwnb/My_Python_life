#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado 
#e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

tupla = (int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: ")))

print(f"Quantas vezes apareceu o numero 9 {tupla.count(9)}")
if 3 in tupla:
	print(f"Em que posição foi digitado o primeiro valor 3 {tupla.index(3)}")
else:
	print("O numero 3 não apareceu nenhuma vez")
print("Segue os numeros pares")
for i in tupla:
	if i % 2 == 0:
		print(i, end=' ')

print()
