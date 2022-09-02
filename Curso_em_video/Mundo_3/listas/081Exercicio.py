#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


lista = list()
while True:
	lista.append(int(input("Entre com um valor: ")))
	resp = input("Quer continuar [S/N]")
	if resp in 'Nn':
		break

lista.sort(reverse=True)
print(f"A quantidade de numeros digitados foram {len(lista)}")
print(f"Lista ordenada {lista}")

if 5 in lista:
	print("O valor 5 foi digitado.")
else:
	print("O valor 5 não foi digitado.")
