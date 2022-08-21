#021Exercicio.py
# Faça um programa em python que abra e reproduza
#o audio de um arquivo mp3
#RATM_Killing_In_the_Name.mp3

import pygame

pygame.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
pygame.mixer.music.unload()
