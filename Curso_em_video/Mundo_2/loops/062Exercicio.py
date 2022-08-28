#062Exercicio.py
# Refaça o exercicio 061 e pergunte ao usuário se ele quer mais alguns termos.
# Para sair o usuário deve digitar 0 em termos.


n = 0
count = 0
while True:
	if count == 0:
		value = int(input("If you want to exit enter with 0 :"))
		if value == 0:
			break
		else:
			count = 1
	elif count != 0:
		term = int(input("Enter with the first term: "))
		ratio = int(input("Enter with the ratio: "))
		count = 0
		n = 0
		while n < 10:
			print(term)
			term = term + ratio
			n += 1
