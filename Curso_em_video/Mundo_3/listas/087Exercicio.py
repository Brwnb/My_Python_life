#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:   
#A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
	for j in range(3):
		matriz[i][j] = int(input(f"Digite um valor[{i},{j}]: "))

maior = 0
soma = 0
pares = 0
for i in range(3):
	for j in range(3):
		if matriz[i][j] % 2 == 0:
			pares += matriz[i][j]
		if j == 2:
			soma += matriz[i][j]
		print(f'[{matriz[i][j]}]', end='')
	print()


for m in range(3):
	if m == 0:
		maior = matriz[1][m]
	elif matriz[1][m] > maior:
		maior = matriz[1][m]

print(f'pares: {pares}')
print(f"Soma: {soma}")
print(f'Maior {maior}')