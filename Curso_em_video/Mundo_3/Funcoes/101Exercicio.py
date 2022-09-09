#Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(valor):
	idade = date.today().year - valor
	if idade < 16:
		return 'NEGADO'
	elif 16 < idade < 18:
		return 'OPCIONAL'
	else:
		return 'OBRIGATÓRIO'


dever = voto(int(input('Digite o ano do seu nascimento: ')))

print(f'O ano digitado diz que é: {dever} votar')