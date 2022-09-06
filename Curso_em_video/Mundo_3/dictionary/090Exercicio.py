#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a 
#situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
#media 7 > passou / entre 5 e 6.9 recuperação / < 5 reprovado

aluno = dict()
aluno['nome'] = input('Entre com o nome do aluno: ')
aluno['media'] = float(input('Entre com a média do aluno: '))




if aluno['media'] >= 7:
	aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7 and aluno['media'] >= 5:
	aluno['situacao'] = 'Recuperacao'
else:
	aluno['situacao'] = 'Reprovado'

for i,j in aluno.items():
	print(f'{i} é igual a {j}')

"""
print(f'O aluno {aluno["nome"]}')
print(f'Possui média {aluno["media"]}')
print(f'A situação do aluno é {aluno["situacao"]}')
"""



"""
print(f'O aluno {aluno["nome"]}')
print(f'Possui média {aluno["media"]}')

if aluno['media'] >= 7:
	print("A situação do aluno aprovado!!!")
elif aluno['media'] < 7 and aluno['media'] >= 5:
	print('A situação do aluno é recuperação!!!')
else:
	print('Aluno Reprovado!!!')


"""

