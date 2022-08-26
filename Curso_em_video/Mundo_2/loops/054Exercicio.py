#054Exercicio.py
#Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas 
#já são maiores. A maior idade será com 21 anos.

from datetime import date
count_majority = 0
count_minority = 0
for i in range(7):
	year = int(input("Enter with a year: "))
	today = date.today().year
	value = today - year
	if value < 21:
		count_minority += 1
	else:
		count_majority += 1

print("The quantity of Majority is {}. ".format(count_majority))
print("The quantity fo Minority is {}".format(count_minority))