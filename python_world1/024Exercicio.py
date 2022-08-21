#024Exercicio
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "Santo".

city = input("Enter with the city's name: ").upper().strip()
print(city[:5] == "SANTO")