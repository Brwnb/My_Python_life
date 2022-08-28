#Faça uma progreção aritimetica lendo o primeiro termo e a sua razão. 
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

term = int(input("Enter with the first term: "))
ratio = int(input("Enter with the ratio: "))

n = 0
while n < 10:
	print(term)
	term = term + ratio
	n += 1

