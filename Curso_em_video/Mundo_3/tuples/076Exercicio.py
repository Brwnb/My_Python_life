#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência. No final, 
#mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
	'maça',1.70,
	'Banana',2.50,
	'abacaxi',4.10, 
	'mamão', 4.90,
	'melancia', 1.10
	)
for prod in range(0, len(produtos)):
	if prod % 2 == 0:
		print(f"{produtos[prod]:.<14}", end="")
	else:
		print(f"R$ {produtos[prod]:.2f}")

