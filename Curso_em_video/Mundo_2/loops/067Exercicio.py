 #067Exercicio.py
 #Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será #interrompido quando
 # o número solicitado for negativo. 

cond = 0
print("Tabuada para sair digite qualquer valor negativo")
while True:
    cond = int(input("Digite um número: "))
    count = 0
    if cond < 0:
        break
    while count < 11:
        print(cond * count)
        count += 1

