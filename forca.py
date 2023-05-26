import pygame as pg
import random

#Cores para usar no jogo
branco = (255,255,255)
preto = (0,0,0)

#Setup da tela do jogo
Window = pg.display.set_mode((1000,600))

# Iniciando a fonto da forca
pg.font.init()
#Fonte e tamanho
font = pg.font.SysFont('Courier New', 50)
font_rb = pg.font.SysFont('Courier New', 30)

palavras = [
    "SISTEMA"
    "TECNOLOGIA"
    "COMPUTADOR"
    "SITE"
]

#Variaveis
tentativas_de_letras = ['','_']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chanches = 0
letra = ''
click_last_status = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #TELA DO JOGO
    pg.display.update()