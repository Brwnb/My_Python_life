#079Exercicio.py
#Exercício Python 079: Crie um programa onde o usuário possa digitar 
#vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
count = 4
value = list()
for i in range(5):
	if i == 0:
		value.append(int(input("Digite alguns valores: ")))
	else:
		while count > 0:
			temp = int(input("Digite alguns valores: "))
			if temp in value:
				print("This number already entered. Try another one")
			else:
				value.append(temp)
				count -= 1
value.sort()
print(f"The number entered were {value}")