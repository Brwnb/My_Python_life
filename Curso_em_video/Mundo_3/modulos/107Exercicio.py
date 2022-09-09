"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from matematica import utils
value = int(input("Enter with a value: "))

print(f'The {value}  with 10% is {utils.aumentar(value,10)}')
"""
diminuir(value)
dobro(value)
metade(value)
"""