#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou 
#não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
##B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

age = 0
sex =''
age_people = 0
age_female = 0
count_male = 0
count_female = 0
while True:
	sex = input("Enter with your sex[M/F]: ").upper()
	age = int(input("Enter with your age: "))

	if sex == 'M':
		count_male += 1
		if age > 18:
			age_people += 1
	elif sex == 'F':
		count_female += 1
		if age < 20:
			age_female += 1
		if age > 18:
			age_people += 1
			print(age_people)

	stop = input("If you want to stop typed [Y/N]").upper()
	if stop == 'Y':
		break

print(f"Quantity of Female is {count_female}")
print(f"Quantity of male is {count_male}")
print(f"Quantity of women with 20 year or less is {age_female}")
print(f"Quantity of people with 18 year or more is {age_people}")