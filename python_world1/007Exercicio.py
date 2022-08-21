# escreva um programa que leia um valor em em metros e o exiba convertido em centimetros e milimetros.

value = int(input("Enter a value"))

print("The {} meters is {} centimeters and {} milimiters".format(value, value*100, value*1000))