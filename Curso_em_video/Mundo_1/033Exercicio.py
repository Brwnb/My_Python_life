#033Exercicio.py
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input("Enter with a first value: "))
num2 = int(input("Enter with the second value: "))
num3 = int(input("Enter with the third: "))

biggest = 0
smallest = 0
if num1 > num2 and num1 > num3:
	biggest = num1
	if num2 < num3:
		smallest = num2
	else:
		smallest = num3
elif num2 > num1 and num2 > num3:
	biggest = num2
	if num1 < num3:
		smallest = num1
	else:
		smallest = num3
else:
	biggest = num3
	if num1 < num2:
		smallest = num1
	else:
		smallest = num2

print("The biggest number is: {}".format(biggest))
print("The smallest number is {}".format(smallest))
