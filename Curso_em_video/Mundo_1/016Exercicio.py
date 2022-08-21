#016Exercicio
# Crie um programa que leia um número real qualquer pelo 
# teclado e mostre na tela a sua porção inteira.

from math import trunc

value = float(input("Enter with a value: "))
print("The value is {}".format(trunc(value)))
