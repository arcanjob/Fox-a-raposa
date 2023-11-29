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
fase = 1

while True:
    
    MAPA = MAPAS[f'MAPA{fase}']  #chama todos os mapas, de acordo com a variação das fases
    if estado_do_jogo == jogando: #está no jogo
        estado_do_jogo = tela_do_jogo(janela, fase, MAPA)
        if fase == 3: #se vem pra ca e a fase é 3, significa que o jogo acabou
            fase = 1
            estado_do_jogo = INICIO #entao o jogo reinicia
    elif estado_do_jogo == INICIO:
        estado_do_jogo = tela_inicial_de_texto(janela)

    elif estado_do_jogo == morreu_de_vez: #perdeu as tres vidas
        estado_do_jogo = tela_de_derrota(janela)

    elif estado_do_jogo == vitoria:
        x = tela_de_vitoria(janela, fase) #ele uem adicionara um nivel por fase
        fase = x[0]
        estado_do_jogo = x[1]
        
