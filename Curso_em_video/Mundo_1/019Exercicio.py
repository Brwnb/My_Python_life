#019Exercicio.py
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o 
# nome do escolhido

import random
aluno1 = input("Enter with the student name: ")
aluno2 = input("Enter with the student name: ")
aluno3 = input("Enter with the student name: ")
aluno4 = input("Enter with the student name: ")
temp = [aluno1, aluno2, aluno3, aluno4]
print("The student is {}".format(random.choice(temp)))
