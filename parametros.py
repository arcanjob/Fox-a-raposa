# pylint: disable=missing-module-docstring
import pygame
pygame.mixer.init()
pygame.init()

FPS = 60 # Frames por segundo

janela = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Hello World!')

####TAMANHOS
#JANELA
LARGURA_JANELA = 1000 # Largura da tela - A DEFINIR
ALTURA_JANELA =  600# Altura da tela - A DEFINIR

#FUNDO
LARGURA_FUNDO = LARGURA_JANELA
ALTURA_FUNDO = LARGURA_JANELA

#ESPINHOS
LARGURA_ESPINHOS = 30 #A DEFINIR
ALTURA_ESPINHOS = 20 #A DEFINIR

#JOGADOR
ALTURA_JOGADOR= 20 #A DEFINIR
LARGURA_JOGADOR = 7 #A DEFINIR

#PLATAFORMA
ALTURA_PLATAFORMA = 20 #A DEFINIR
LARGURA_PLATAFORMA = 20 #A DEFINIR

#MOEDA
ALTURA_MOEDA = 5
LARGURA_MOEDA = 5


# Estabelecer as figuras
img_personagem = pygame.image.load('imagens_e_sons/imagens/raposa/raposa_andando/Walk (1).png').convert_alpha()
img_fundo = pygame.image.load('imagens_e_sons/fundo/Fundo_jogo.jpg').convert_alpha()
#img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataformas.png').convert_alpha()
#img_moeda = pygame.image.load('imagens_e_sons/imagens/moeda.png').convert_alpha()






#POSIÇÃO INICIAL DO JOGADOR - A DEFINIR
x_meio_inicial_do_personagem = 32
y_peh_inicial_do_personagem = 23


# CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)


# Estados para controle do fluxo da aplicação
INICIO = 0
JOGO = 1
FIM = 2
