#020Exercicio.py
# O professor quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
# ordem sorteada.
import random

aluno1 = input("Enter with the student name: ")
aluno2 = input("Enter with the student name: ")
aluno3 = input("Enter with the student name: ")
aluno4 = input("Enter with the student name: ")
temp = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(temp)
print("The student is {}".format(temp))
