import pygame
pygame.mixer.init()
pygame.init()

FPS = 60 # Frames por segundo

velocidade_de_rotaca_p_frame = 1 # do personagem, ao cair

JANELA = pygame.display.set_mode((1000, 500))
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
img_personagem = pygame.image.load('imagens_e_sons/imagens/garoto/garoto_parado/Idle (1)').convert_alpha()
img_fundo = pygame.image.load('imagens_e_sons/fundo/Fundo_jogo.jpg').convert_alpha()
img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
img_moeda = pygame.image.load('imagens_e_sons/imagens/moeda.png').convert_alpha()
img_espinhos = pygame.image.load('imagens_e_sons/imagens/espinho.png').convert_alpha()
img_coracoes = pygame.image.load('imagens_e_sons/imagens/coracao.png').convert_alpha()


#REDIMENSIONANDO AS FIGURAS
#redimensionando as imagens
#image = pygame.transform.scale(image, (125, 166)) para obter uma nova imagem de 125 X 166 pixels.
img_fundo = pygame.transform.scale(img_fundo, (LARGURA_FUNDO, ALTURA_FUNDO))
img_personagem = pygame.transform.scale(img_personagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
img_plataformas = pygame.transform.scale(img_plataformas, (LARGURA_PLATAFORMA, ALTURA_PLATAFORMA))
img_moeda = pygame.transform.scale(img_moeda, (LARGURA_MOEDA, ALTURA_MOEDA))
img_espinhos = pygame.transform.scale(img_espinhos, (LARGURA_ESPINHOS, ALTURA_ESPINHOS))




#TEXTO
fonte_pontos =  pygame.font.Font('fontes/pontuacao.ttf', 28)


#ESTABELECER OS SONS
som_fundo = pygame.mixer.music.load('imagens_e_sons/sons/fundo.ogg')
pygame.mixer.music.set_volume(0.4)

som_caindo = pygame.mixer.Sound('imagens_e_sons/sons/caindo.wav')
som_pegando_moedas = pygame.mixer.Sound('imagens_e_sons/sons/moedas.wav')
som_caido = pygame.mixer.music.load('imagens_e_sons/sons/caido.ogg')
som_morrendo = pygame.mixer.music.load('imagens_e_sons/sons/morrendo.ogg')
som_game_over =pygame.mixer.music.load('imagens_e_sons/sons/game_over.ogg')
som_perdendo_vida =  pygame.mixer.music.load('imagens_e_sons/sons/perdendo_vida.ogg')


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



####################******************ANIMAÇÕES - PRO GRAND FINALE
anim_morrendo = []
arquivo_morrendo = 'imagens_e_sons/imagens/garoto/garoto_morrendo'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_morrendo, f'Dead ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_morrendo.append(img)

anim_parado = []
arquivo_parado = 'imagens_e_sons/imagens/garoto/garoto_parado'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_parado, f'Idle ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_parado.append(img)


anim_pulando = []
arquivo_pulando = 'imagens_e_sons/imagens/garoto/garoto_pulando'
for i in range(15):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(arquivo_pulando, f'Jump ({i+1}).png')
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        anim_parado.append(img)

