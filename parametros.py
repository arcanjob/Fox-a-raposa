pygame.mixer.init()



# Estabelecer as figuras
img_personagem = pygame.image.load('imagens_e_sons/imagens/personagem.png').convert_alpha()
img_fundo = pygame.image.load('imagens_e_sons/imagens/fundo.png').convert_alpha()
img_espinhos = pygame.image.load('imagens_e_sons/imagens/espinhos.png').convert_alpha()
img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataformas.png').convert_alpha()

#ESTABELECER OS SONS
som_batida =  pygame.mixer.Sound('imagens_e_sons/sons/batida.wav')
som_caindo = pygame.mixer.Sound('imagens_e_sons/sons/caindo.wav')
som_fundo = pygame.mixer.music.load('imagens_e_sons/sons/fundo.ogg')



#def parametros():
# Dados gerais do jogo.
LARGURA_JANELA = 1000 # Largura da tela - A DEFINIR
ALTURA_JANELA =  600# Altura da tela - A DEFINIR
FPS = 60 # Frames por segundo

# Define tamanhos
LARGURA_ESPINHOS = 30 #A DEFINIR
ALTURA_ESPINHOS = 20 #A DEFINIR
ALTURA_JOGADOR = 20 #A DEFINIR
LARGURA_JOGADOR = 7 #A DEFINIR


"""
# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

"""

# Estados para controle do fluxo da aplicação
INICIO = 0
JOGO = 1
FIM = 2
