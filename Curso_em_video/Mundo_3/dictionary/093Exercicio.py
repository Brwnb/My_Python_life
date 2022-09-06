#Exercício Python 093: Crie um programa que gerencie o aproveitamento de 
#um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

estatistica = dict()
guardar = list()

estatistica['nome'] = input("Nome do jogador: ")
total_partidas = int(input("Quantidade de Partidas: "))
for p in range(total_partidas):
	guardar.append(int(input(f"Quantos gols na partida {p+1}?: ")))
estatistica['gols'] = guardar[:]
estatistica['total'] = sum(guardar)
#print(estatistica)

for i, v in enumerate(estatistica['gols']):
	print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {estatistica["total"]} gols')