#049Exercicio.py
#Faça uma tabuade de um número digitado pelo usuário.

value = int(input("Enter with the value: "))
print("Tabuada do {}".format(value))
for i in range(0,11):
	print(value * i)
