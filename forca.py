import pygame as pg
import random

#Cores para usar no jogo
branco = (255,255,255)
preto = (0,0,0)

#Setup da tela do jogo
window = pg.display.set_mode((1000,600))

# Iniciando a fonto da forca
pg.font.init()
#Fonte e tamanho
font = pg.font.SysFont('Courier New', 50)
font_rb = pg.font.SysFont('Courier New', 30)

palavras = [
    "SISTEMA",
    "TECNOLOGIA",
    "COMPUTADOR",
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

#FUNCTION PARA DESENHAR
def Desenho_da_forca(window, chanches):
    pg.draw.rect(window, branco, (0,0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100,100), 10)
    pg.draw.line(window, preto, (50, 500), (150,500), 10)
    pg.draw.line(window, preto, (100, 100), (300,100), 10)
    pg.draw.line(window, preto, (300, 100), (300,150), 10)
    if chanches >= 1:
        pg.draw.circle(window, preto, (300,200), 50,10)
    if chanches >= 2:
        pg.draw.line(window, preto, (300,250), (300, 350), 10)
    if chanches >= 3:
        pg.draw.line(window, preto, (300,260), (225, 350), 10)
    if chanches >= 4:
        pg.draw.line(window, preto, (300,260), (375, 350), 10)
    if chanches >= 5:
        pg.draw.line(window, preto, (300,350), (375, 450), 10)
    if chanches >= 6:
        pg.draw.line(window, preto, (300,350), (225, 450), 10)


#BOTÃO DE RESTART
def Desenho_Resetart_Button(window):
    pg.draw.rect(window, preto, (700, 100, 200, 65))
    texto = font_rb.render('Restart', True, branco)
    window.blit(texto,(740, 120))


#SORTEIO DE UMA PALAVRA
def sorteio(palavras, palavra_escolhida, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(palavras)-1)
        palavra_escolhida = palavras[palavra_n]
        end_game = False
    return palavra_escolhida, end_game


#Function para camuflar a palavra
def camuflar(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n +1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '_')
    return palavra_camuflada

#TENTATIVA DE LETRA

def tentativa(tentativas_de_letras,palavra_escolhida, letra, chanche):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chanche += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras,chanche

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()
            print(letra)

    #FUCTION JOGO
    Desenho_da_forca(window, 6)
    Desenho_Resetart_Button(window)
    palavra_escolhida, end_game = sorteio(palavras, palavra_escolhida, end_game)
    palavra_camuflada = camuflar(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras,chanche = tentativa(tentativas_de_letras,palavra_escolhida, letra, chanche)
    print(palavra_escolhida, palavra_camuflada)
    pg.display.update()