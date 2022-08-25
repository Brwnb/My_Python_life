#051Exercicio.py
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA  (Progressão aritimetica).
# No final, mostre os 10 primeiros termos dessa progressão.

first = int(input("First term: "))
ratio = int(input("Enter with a ratio: "))
temp = first + (10 - 1) * ratio
for i in range(first, temp + ratio, ratio):
	print(i, end=' -> ')