#023Exercicio
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. (milhar,centenas, dezenas e unidades)

value = input("Enter a value: ")
temp = value[0:4]
print("Milhar: {}".format(temp[0]))
print("Centena: {}".format(temp[1]))
print("Dezena: {}".format(temp[2]))
print("Unidade: {}".format(temp[3]))