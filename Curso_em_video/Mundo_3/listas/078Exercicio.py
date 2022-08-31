#078Exercicio.py
#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na 
#lista.

maior = menor = 0
value = list()
for i in range(5):
	value.append(int(input("Digite alguns valores: ")))
	if i == 0:
		menor = maior = value[i]
	else:
		if value[i] > maior:
			maior = value[i]
		if value[i] < menor:
			menor = value[i]

print(f"Valores digitados{value}")
print(f"O maior valor é {maior} nas posições ", end ="")
for a,b in enumerate(value):
	if b == maior:
		print(f"{a}, ", end="")
print()

print(f"O menor valor é {menor} nas posições ", end="")
for a,b in enumerate(value):
	if b == menor:
		print(f"{a}, ", end="")

print()

# Usando funções do python
#print(f"O maior valor é {max(value)}")
#print(f"O menor valor é {min(value)}")
