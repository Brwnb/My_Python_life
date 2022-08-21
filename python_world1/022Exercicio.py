#022Exercicio
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minusculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome.

frase = input("Type your name: ")
newfrase=frase.replace(" ","").strip()
size_name=frase.strip().split()

print("Your name is {} ".format(frase.upper()))
print("Your name is {} ".format(frase.lower()))
print("the size of your name is without space is {} ".format(len(newfrase)))
print("The size of the first name is {}".format(len(size_name[0])))
print("Your name with The first Letter upper is {}".format(frase.title()))