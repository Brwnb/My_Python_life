#026 Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "A"
# Em que posição a primeira vez
# Em que posição ela aparece a última vez

name = input("Enter with your name: ").strip().upper().strip()
print("The letter A appear {}".format(name.count('A')))
print("The letter A appear in the last positions {}".format(name.rfind('A')+1))
print("The letter A appear in the fist positions {}".format(name.find('A')+1))