#054Exercicio.py
#Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas 
#já são maiores. A maior idade será com 21 anos.

count_majority
count_minority
for i in range(7):
	value = int(input("Enter with a value: "))
	if value < 21:
		count_minority += 1
	else:
		count_majority

print("The quantity of Majority is {}. ".format(count_majority))
print("The quantity fo Minority is {}".format(count_minority))