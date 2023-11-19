import pygame
from parametros import *
from tela_inicial import *
from sprites_e_classes import *

pygame.init()

window = pygame.display.set_mode((1000, 600))



# CRIANDO A JANELA
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('NOSSO JOGO')



###############CRIANDO AS PLATAFORMAS




estado_do_jogo = INICIO

game = True
#iniciando o loop
while game:
    ultimo_pulo = pygame.time.get_tics()
    #analisa se o jogo foi fechado
    for envent in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if estado_do_jogo == INICIO:
        estado_do_jogo = tela_inicial(JANELA)
    
    if estado_do_jogo == JOGO:
        estado_do_jogo = jogando(JANELA)

    else:
        estado_do_jogo = tela_final(JANELA)



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

