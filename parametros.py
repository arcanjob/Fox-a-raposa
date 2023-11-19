#import pygame

#pygame.mixer.init()

FPS = 60 # Frames por segundo

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
img_personagem = pygame.image.load('imagens_e_sons/imagens/personagem.png').convert_alpha()
img_fundo = pygame.image.load('imagens_e_sons/imagens/fundo.png').convert_alpha()
img_espinhos = pygame.image.load('imagens_e_sons/imagens/espinhos.png').convert_alpha()
img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataformas.png').convert_alpha()
img_moeda = pygame.image.load('imagens_e_sons/imagens/moeda.png').convert_alpha()



#redimensionando as imagens
#image = pygame.transform.scale(image, (125, 166)) para obter uma nova imagem de 125 X 166 pixels.
img_espinhos = pygame.transform.scale(img_espinhos, (LARGURA_ESPINHOS, ALTURA_ESPINHOS))
img_fundo = pygame.transform.scale(img_fundo, (LARGURA_FUNDO, ALTURA_FUNDO))
img_personagem = pygame.transform.scale(img_personagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
img_plataformas = pygame.transform.scale(img_plataformas, (LARGURA_PLATAFORMA, ALTURA_PLATAFORMA))
img_moeda = pygame.transform.scale(img_moeda, (LARGURA_MOEDA, ALTURA_MOEDA))

#ESTABELECER OS SONS
som_dano =  pygame.mixer.Sound('imagens_e_sons/sons/batida.wav')
som_caindo = pygame.mixer.Sound('imagens_e_sons/sons/caindo.wav')
som_fundo = pygame.mixer.music.load('imagens_e_sons/sons/fundo.ogg')
som_game_over = pygame.mixer.Sound('imagens_e_sons/sons/game_over.wav')
som_pegando_a_moeda = pygame.mixer.Sound('imagens_e_sons/sons/moeda.wav')


#POSIÇÃO INICIAL DO JOGADOR - A DEFINIR
x_meio_ininicial_do_personagem = 32
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
