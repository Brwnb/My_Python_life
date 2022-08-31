#078Exercicio.py
#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na 
#lista.
value = list()
for i in range(5):
	value.append(int(input("Digite alguns valores: ")))

print(f"O maior valor é {max(value)}")
print(f"O menor valor é {min(value)}")
