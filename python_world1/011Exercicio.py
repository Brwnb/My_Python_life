# Faça um programa que leia a largura de uma parede em metros
# calcule sua área e a quantidade de tinta necessário apra pintá-lo, 
# sabendo que cada litro de tinta pinta uma área de 2m².

height = int(input("Enter the height value: "))
width = int(input("Enter the widht value: "))

area = height*width
ink = area/2
print("The area of wall is {}. The quantity of ink is {}.".format(area, ink))

