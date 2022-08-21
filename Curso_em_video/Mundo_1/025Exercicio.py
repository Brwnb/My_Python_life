#Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome

name = input("Enter a name: ").strip().upper()

print("The name SILVA: {}".format("SILVA" in name))
