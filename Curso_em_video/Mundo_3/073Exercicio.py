#073Exercicio.py
#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
#Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',\
	'São Paulo', 'Atlético Mineiro', 'Athletico-PR', 'Cruzeiro',\
	'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', \
	'Chapecoense', 'Ceará', 'Vasco da Gama', 'Sport Recife', 'América-MG', \
	'Vitória', 'Paraná')

print(f'Os cinco primeiros times: ')
for i in range(5):
	print(f"{i+1}-{times[i]}")

print('=-='*10)
print(f'Os quatros ultimos times: ')
for c in range(4):
	print(f"{c+17}-{times[c+16]}")


ordenado = tuple(sorted((times)))
print('=-='*10)
print("Todos os times por ordem alfabética")
for a in range(len(ordenado) - 1):
	print(ordenado[a])

print('=-='*10)
for i in range(len(times)-1):
	if times[i] == 'Chapecoense':
		print(f"A Chapecoence ficou na {i+1} posição")
