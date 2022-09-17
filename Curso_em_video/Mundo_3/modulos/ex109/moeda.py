def aumentar(preco, taxa, formato=False):
	result = preco + (preco * taxa/100)
	return result if formato is False else moeda(result)


def diminuir(preco, taxa, formato=False):
	result = preco - (preco * taxa/100)
	return result if formato is False else moeda(result)


def dobro(preco, formato=False):
	result = preco + preco
	return result if formato is False else moeda(result)


def metade(preco, formato=False):
	result = preco / 2
	return result if formato is False else moeda(result)

def moeda(preco,moeda='RS'):
	return f'{moeda} {preco:.2f}'.replace('.',',')