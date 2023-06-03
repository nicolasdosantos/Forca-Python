import pygame
from pygame.locals import *
import random
from text import Text

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

# Colisão da cobra om a maça
def collision(pos1, pos2):
    return pos1 == pos2

#Limites do mapa
def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

# Randomização 
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

#Cobra 
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT
pontos = 0

#Variavel de texto 
text_ponto = Text("ShareTechMono-Regular.ttf", 25, str(pontos),(255, 255, 255), [10,10])

#Apple
apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

#Reset do jogo após a morte
def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()
    global pontos
    pontos = 0
    text_ponto.update_text(str(pontos))

#Clico do jogo / Pontos / Morte / Comandos
while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)
    text_ponto.drawFade()

    #Colisão da cobra com a maçã, contando pontos 
    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        pontos += 1
        text_ponto.update_text(str(pontos))

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    #Tamanho do desenho da cobra
    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
            break
        snake_pos[i] = snake_pos[i - 1]

    #Limites onde pode ir, com o reset do jogo
    if off_limits(snake_pos[0]):
        restart_game()

    #Dirição da cobra, com a tecla da setinha 
    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()