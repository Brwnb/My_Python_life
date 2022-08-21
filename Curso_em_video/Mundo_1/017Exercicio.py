#017Exercicio.py
# Faça um programa que leia o comprimento do cateto posto
# e do cateto adjacente de um triangulo retângulo, Calcule e
# mostre o comprimento da hipotenusa.format

from math import hypot
cateto = float(input("Enter with a number: "))
adj = float(input("Enter with a outher number: "))

print("Them hipotenuses is {:.2f}".format(hypot(cateto,adj)))
