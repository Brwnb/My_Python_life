#035Exercicio.py
# Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo
lado1 = float(input("Enter with a first value: "))
lado2 = float(input("Enter with the second value: "))
lado3 = float(input("Enter with the third: "))

if lado2 - lado3 < lado1 and lado1 < lado2 + lado3:
	if lado3 - lado1 < lado2 and lado2 < lado3 + lado1:
		if lado1 - lado2 < lado3 and lado3 < lado2 + lado3:
			print("it's a triangle")
		else:
			print("it's not a triangle *")
	else:
		print("it's not a triangle **")
else:
	print("it'a not a triangle ***")