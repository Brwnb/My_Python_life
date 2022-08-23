#041Exercicio.py
#A confederação Nacional de natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: Sênior
# Acima: Master

age = int(input("Enter with the birth year: "))

if age < 10 and age >0:
	print("The kid will be classifield as mirim")
elif age >=10 and age <15:
	print("The kid will be classifield as infatil")
elif age >= 15 and age < 20:
	print("The youth will be classifield as Junior")
elif age == 20:
	print("The youth will be classfield as Sênior")
elif age > 20:
	print("The youth will be classifield as Master")
else:
	print("Enter with a valid value")
