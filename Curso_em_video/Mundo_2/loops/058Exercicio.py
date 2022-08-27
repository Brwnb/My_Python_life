#058Exercicio.py
#Adivinhe o número que o computador esta pensando.
# Os números vão de 0 a 10. Tente até conseguir acertar.

from random import randint

sort = randint(0, 10)
run = True
while run:
	value = int(input("Enter with a value between 0 and 10: "))
	if value == sort:
		print("CONGRATS. YOU WON!!!")
		run = False
	else:
		print("Try Again")
		run = True

