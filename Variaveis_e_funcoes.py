
#Chama todas as bibliotécas que serão usadas ao longo de todo o código
import pygame
import random
from os import path

#inicializa  o pygame
pygame.init()
#inicializa  o pygame mixer (parte que controla o som)
pygame.mixer.init()

#Define as variáveis que controlarão o jogo, 
jogando = 0
DONE = 1
inicio = 3
bonequinho = "Imagem"

#Define o relógio a ser usado durante todo o jogo
clock = pygame.time.Clock()

#Define a imagem de inicio, a famosa tela inicial
img_inicio = pygame.image.load('imagens_e_sons/imagens/inicio.png')#tela inicial 

#define qual será o título do jogo, muito criativo
TITULO = 'Fox, a raposa'

#Variáveis de dimensionamento da janela principal, largura e altura
largura = 1350
altura = 680 

#Define o tamanho dos azulejos do jogo (o piso)
tamanho_azulejo = 40

#define o tamanho do jogador, a nossa raposa, com relação ao tamanho do azulejo
largura_do_jogador = tamanho_azulejo
altura_do_jogador = int(tamanho_azulejo * 1)

#Define a taxa de frames do jogo
FPS = 60

#Define a cor preta
BLACK = (0, 0, 0)

#velocidade_de_queda = 5

#quanto_pula = tamanho_azulejo

#define a velocidade no eixo x (esquerda e direita)
velocidade_no_eixo_x = 20

#Variáveis usadas na contrução do mapa
#A variável "B" define o que é um bloco
B = 1

#Define os espaços que ficarão vazios
V = 2

#Define onde estarão as galinhas que a raposa irá buscar
G = 3

#As próximas 5 variáveis vão definir o que é um espinho e para qual lado ele irá apontar
ED = 4
EE = 5
EB = 6
EB = 7
E = 10

#A variável "O" define o ponto final, uma espécie de portal pelo qual a raposa tenta chegar
O = 8

#O "R" vai definir em que parte do mapa a raposa irá ser gerada
R = 9


#O mapa em si, em que cada variável acima é chamada e preeenche um espaço do mapa
MAPA =[
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,O,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,G,V,V,V,V,V,V,B,B],
    [ED,V,V,V,V,G,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,G,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,R,V,V,V,V,V,V,V,V,V,V,V,G,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]


#Variáveis que irão ser usada para definir o estado do jogador
paradinho = 0
pulando = 1
caindo = 2

#Cria a função 
class azulejo(pygame.sprite.Sprite):

    # Constrói a classe
    def __init__(self, foto_do_azulejo, filas, colunas):
        
        pygame.sprite.Sprite.__init__(self)

        #adicona a foto do azulejo a uma variável
        foto_do_azulejo = pygame.transform.scale(foto_do_azulejo, (tamanho_azulejo, tamanho_azulejo))


#ORIENTACAO
de_peh = 0
com_o_peh_pra_direita = 90
com_o_peh_pra_esquerda = 270
de_ponta_cabeca = 180


class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, foto_do_azulejo, filas, colunas, orientacao):
        
        pygame.sprite.Sprite.__init__(self)

        
        foto_do_azulejo = pygame.transform.rotate(pygame.transform.scale(foto_do_azulejo, (tamanho_azulejo, tamanho_azulejo)), orientacao)

        #Puxa as imagens
        self.image = foto_do_azulejo
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect()
        self.rect = self.image.get_rect()

        #define o tamanho dos azulejos
        self.rect.x = tamanho_azulejo * colunas
        self.rect.y = tamanho_azulejo * filas


#Cria o jogador definindo a sua classe
class Player(pygame.sprite.Sprite):

    def __init__(self, bonequinho, filas, colunas, piso_parede):
        #Chama a função do sprite
        pygame.sprite.Sprite.__init__(self)

        self.estado_do_jogo = paradinho
        #define o tamanho do boneco
        bonequinho = pygame.transform.scale(bonequinho, (largura_do_jogador, altura_do_jogador))

        #puxa as imagens
        self.image = bonequinho
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect()
        self.rect = self.image.get_rect()
        self.piso_parede = piso_parede
        self.rect.x = colunas * tamanho_azulejo
        self.rect.bottom = filas * tamanho_azulejo

        self.speedx = 0
        self.speedy = 0
    
    #Função resposável por definir as atualizações de estado
    def update(self):

        if self.speedy != 0 or self.speedx != 0:

            self.estado_do_jogo = caindo
        
        self.rect.y += self.speedy
        
        #define o dicionário que será criado caso haja colisões
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False, pygame.sprite.collide_mask)
        
        #confere as colisões no topo e na base
        for colisao in colisoes:
            
            #confere se a velocidade está ou não mais 
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                self.speedy = 0

           #confere se a velocidade está ou não mais 
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                self.speedy = 0

        #confere se a velocidade está ou não mais 
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= largura:
            self.rect.right = largura - 1
        
        #define o dicionário que será criado caso haja colisões
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False, pygame.sprite.collide_mask)
        

        #Confere as colisões na esquerda e na direita
        for colisao in colisoes:
            
            #confere se a velocidade está ou não mais 
            if self.speedx > 0:
                self.rect.right = colisao.rect.left #+largura_do_jogador/2
                self.speedx = 0
            #confere se a velocidade está ou não mais 
            elif self.speedx < 0:
                self.rect.left = colisao.rect.right 
                self.speedx = 0




