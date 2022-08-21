#027 Faça um programa que leia o nome completo de uma pessoa
# mostrando o primeiro e o ultimo nome separadamente

name = input("Enter of the name: ").strip()

temp=name.split()
print("The first name is {}".format(temp[0]))
print("The last name is {}".format(temp[len(temp)-1]))