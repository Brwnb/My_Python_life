#050Exercicio.py
#Deselvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que 
#forem pares. Se o valor digitado for impar desconsidere-o

plus = 0
for i in range (6):
	value = int(input("Enter with a value: "))
	if value % 2 == 0:
			plus = plus + value
print("The sum of pair numbers are {}".format(plus))