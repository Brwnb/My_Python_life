#066Exercicio.py
#Crie um programa que leia números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
#mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

count = 0
value = 0
num = 0
while num != 999:
	num = int(input("Enter with a value: "))
	
	if num == 999:
		break

	value += num
	count += 1

print(f"The sum of numbers are {value} and the quantity of typed are {count}")