import pygame
from parametros import *
from sprites import *
from sprites_e_classes import *


plataformas = pygame.sprite.Group()

plataformas.add(plataforma(100, 400))

def jogando(JANELA):
    cronometro = pygame.time.Clock()




    while estado_do_jogo == JOGO:
        clock.tick(FPS)

        #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
        colisoes_plataformas = pygame.sprite.spritecollide(personagem, plataformas, False)

        #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
        if colisoes_plataformas:
            if personagem.velocidadex !=0:
                personagem.velocidadex -= personagem.velocidadex  # para o jogador
            elif personagem.velocidadey !=0:
                personagem.velocidadey -= personagem.velocidadey  # para o jogador





        plataformas.draw(screen) 

