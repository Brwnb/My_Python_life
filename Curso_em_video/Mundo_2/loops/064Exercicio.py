#064Exercicio.py
# Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

count = plus = value = quit =0

while quit != '999':
	value = int(input("Enter with a value: "))
	plus = plus + value
	count += 1
	quit = (input("If you want to exit enter with value [999]: "))

print("The quantity of numbers typed was {}".format(count))
print("The sum of the all numbers typed was {}".format(plus))

