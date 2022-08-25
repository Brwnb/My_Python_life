#037Exercicio.py
# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base da conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print("Escolha em qual formato você quer converter os valores digitados:")
print("==hex para Hexadecimal==")
print("==bin para binario==")
print("==oc para octal==")
verifica = input("Entra com uma das oções acima: ")
value = int(input("Enter With A value: "))

if verifica == "bin":
	print("The binary Value is: {}".format(format(value,"b")))
elif verifica == "oc":
	print("The Octal Value is: {}".format(format(value,"o")))
elif verifica == "hex":
	print("The Hex Value is: {}".format(format(value,"x")))
else:
	print("Nenhum valor válido")