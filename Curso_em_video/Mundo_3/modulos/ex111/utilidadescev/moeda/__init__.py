
def aumentar(preco, taxa, formato=False):
	result = preco + (preco * taxa/100)
	return result if formato is False else fixa(result)


def diminuir(preco, taxa, formato=False):
	result = preco - (preco * taxa/100)
	return result if formato is False else fixa(result)


def dobro(preco, formato=False):
	result = preco + preco
	return result if formato is False else fixa(result)


def metade(preco, formato=False):
	result = preco / 2
	return result if formato is False else fixa(result)

def fixa(preco,fixa='RS'):
	return f'{fixa} {preco:.2f}'.replace('.',',')

def resumo(preco,taxa1=10,taxa2=15):
	print(f'Preço analisado: {fixa(preco)}')
	print(f'A metade de {fixa(preco)} é {metade(preco, True)}')
	print(f'O dobro de {fixa(preco)} é {dobro(preco, True)}')
	print(f'Aumentando 10%, temos R$ {aumentar(preco, taxa1, True)}')
	print(f'Diminuindo 15%, temos R$ {diminuir(preco,taxa2, True)}')

