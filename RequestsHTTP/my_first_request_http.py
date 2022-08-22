#O basico do básico de requests http
# com o canal hashtag Programação
# https://www.youtube.com/watch?v=IdviYZIQLlA
# O objetivo desse arquivo é simplesmente entender como funciona requests http
# Nunca tinha feito uma request http no python.
# Então é uma boa forma de tentar adquirir esse conhecimento.

# Vou ter que aprender sobre json também.


#Requests em python
#docs.awesomeapi.com.br

import requests

#requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#print(requisicao)
#Solicitando acesso numa pagina
#r = requests.get('https://lista.mercadolivre.com.br/ps5#D[A:ps5]')
#dic_ml = r.json()
#print(dic_ml)
#Vendo o codigo retornado
#print("Valor do mercado livre: {}".format(r.status_code))

#Lendo o que tem dentro do headers
#print(requisicao.headers)
#print(requisicao.json())

#dicionario = requisicao.json()
#print("O valor do euro é: {}".format(dicionario['EURBRL']['bid']))
#print("O menor valor do euro é: {}".format(dicionario['EURBRL']['low']))

#######################################
#######################################

# Conteudo tirado do canal Corey Schafer
# https://www.youtube.com/watch?v=tb8gHvYlCFs

#re = requests.get('https://xkcd.com/353/')
#print(dir(re))
#print(help(re))
re = requests.get('https://imgs.xkcd.com/comics/python.png')

#print(re.content)
with open('comic.png','wb') as f:
	f.write(re.content)
