#040Exercicio.py
# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida: 
# - média abaxo de 5.0: Reprovado
# - média entre 5.0 e 6.9 : Recuperação
# - média 7.0 ou superior: Aprovado

value1 = float(input("Enter with the first score: "))
value2 = float(input("Enter with the second score: "))

avg = (value1 + value2)/2

if avg < 5:
	print("You failed. Your score was {} ".format(avg))
elif avg >5 and avg < 7:
	print("You are recovering. Your score was {} ".format(avg))
elif avg >=7:
	print("You passed. You score was {}".format(avg))
