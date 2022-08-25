#036Exercicio.py
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar.

# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou 
# então o empréstimo será negado.

house_value = float(input("Enter with a house's value: "))
salary = float(input("Enther with the salary: "))
years = int(input("Enther how much years do you spend to pay: "))

installment = house_value / (years * 12)
temp = salary * 0.3

print(temp)
if temp >= installment:
	print("Congratulation, your loan was released")
else:
	print("Sorry your loan was not approved")