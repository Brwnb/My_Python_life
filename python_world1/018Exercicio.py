#018Exercicio.py
# Faça um programa que leia um angulo qualquer e mostre na tela o volar
# do seno, cosseno e tangente desse angulo.

import math
value = float(input("Enter with a value: "))
radian = math.radians(value)
print("The sine is {:.2f}".format(math.sin(radian)))
print("The cosine is {:.2f}".format(math.cos(radian)))
print("The tangent is {:.2f}".format(math.tan(radian)))
