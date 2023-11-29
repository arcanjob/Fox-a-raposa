#importa as bibliotecas necessárias
import pygame
import random
from Corpo_do_jogo import *
from Variaveis_e_funcoes import *

#inicializa  o pygame
pygame.init()
#inicializa  o pygame mixer (parte que controla o som)
pygame.mixer.init()

#Define e cria a variável em que o jogo irágirar em torno
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(TITULO)

estado_do_jogo = INICIO
FASE = [1,0]
while True:
    FASE = FASE[0]
    if estado_do_jogo == jogando:
        estado_do_jogo = tela_do_jogo(janela)
    elif estado_do_jogo == INICIO:
        estado_do_jogo = tela_inicial_de_texto(janela)
    elif estado_do_jogo == morreu_de_vez:
        estado_do_jogo = tela_de_derrota(janela)
    elif estado_do_jogo == vitoria:
        estado_do_jogo = tela_de_vitoria(janela, FASE)




"""
state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

"""