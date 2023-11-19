import pygame
import random
from parametros import *
from os import path

from parametros import *


def tela_inicial(janela):

    # Carrega o fundo da tela inicial
    janela.blit(img_fundo, (0, 0))
    


    while rodando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for evento in pygame.event.get():
            # Verifica se foi fechado.
            if evento.type == pygame.QUIT:
                state = SAINDO
                running = False

            if evento.type == pygame.KEYUP:
                state = JOGO
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(img_fundo, fundo_rect) #fundo_rect = posição do fundo

        # Depois de desenhar tudo, inverte o display.
        #pygame.display.flip()

    return state
