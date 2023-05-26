from palavraforca import palavra
import pygame as pg
import random

#Cores para usar no jogo
branco = (255,255,255)
preto = (0,0,0)

#Setup da tela do jogo
Window = pg.display.set_mode((1000,600))
letras_usuario =[]
chanches = 5
ganhou = False

while True:
    #criação da logica
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chanches} chanches")
    tentativa = input("Digite uma letra para a forca: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chanches -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False


    if chanches == 0 or ganhou:
        break
if ganhou:
    print(f"Voce ganhou o jogo, a palvra certa era {palavra}!")
else:
    print(f"Voce perdeu o jogo!!, a palvra certa era {palavra}!")

