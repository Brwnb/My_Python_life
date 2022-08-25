#048Exercicio.py
# Faça um programa que calcule a soma entre todos os números impares que são
# Multriplos de 3 e que se encontrem no intervalo de 1 até 500.
plus = 0
for i in range(1,500):
	if i % 3 == 0:
		plus = plus + i
		print(i, end=' ')
print("\n")
print("The total sum is {}".format(plus))
