# pylint: disable=no-member

import pygame
from parametros import *
from tela_inicial import *
from sprites_e_classes import *
from jogando import *
from tela0_de_derrota_e_vitoria import *

pygame.init()


window = pygame.display.set_mode((1000, 600))

# CRIANDO A JANELA
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('NOSSO JOGO')

###############CRIANDO AS PLATAFORMAS


estado_do_jogo = INICIO
FASE = 1
game = True
#iniciando o loop dos estados

while estado_do_jogo != DONE:
    ultimo_pulo = pygame.time.get_tics()
    #analisa se o jogo foi fechado
    for envent in pygame.event.get():
        if event.type == pygame.QUIT:
            estado_do_jogo = DONE
    if estado_do_jogo == INICIO:
        estado_do_jogo = tela_inicial(JANELA)
    if estado_do_jogo == JOGANDO:
        estado_do_jogo = jogando(JANELA)
    if estado_do_jogo == GAME_OVER:
        estado_do_jogo = tela_final(JANELA)
    if estado_do_jogo == VITORIA:
        FASE +=1
        if FASE!=4:
            estado_do_jogo = tela_de_vitoria(JANELA)
        else:
            estado_do_jogo = fim_vitorioso(JANELA)







#fecha a janela
pygame.quit()













game = True


while game:
    
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
            game = False


    window.fill((0, 71, 171)) 
    pygame.display.update()


pygame.quit()

