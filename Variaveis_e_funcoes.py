import pygame
import random
from os import path

pygame.init()
pygame.mixer.init()



jogando = 0
DONE = 1
inicio = 3
clock = pygame.time.Clock()

img_inicio = pygame.image.load('imagens_e_sons/imagens/inicio.png')#tela inicial 



TITULO = 'Fox, a raposa'
largura = 1350
altura = 680 
tamanho_azulejo = 40
largura_do_jogador = tamanho_azulejo
altura_do_jogador = int(tamanho_azulejo * 1.5)
FPS = 60


bonequinho = 'moeda_img'

BLACK = (0, 0, 0)

#velocidade_de_queda = 5

#quanto_pula = tamanho_azulejo

velocidade_no_eixo_x = 10


B = 0
P = B
V = -1
L = B
G = 10
EMPTY = -1
MAPA = [
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,B],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [L,G,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [L,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [L,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [L,P,P,P,P,P,P,V,P,P,P,P,P,P,P,P,P,P,P,V,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [L,B,B,B,B,B,P,V,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,V,V,V,V,V,V,V,L,B],
    [B,V,V,V,V,B,B,V,V,V,B,B,B,B,B,B,B,B,B,B,V,V,V,V,B,B,B,B,B,B,B,B,L,B],
    [L,V,V,V,V,V,B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,L,B],
    [L,V,V,B,B,B,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,L,B],
    [L,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,B,V,B,B,B,P,P,P,P,L,B],
    [L,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,B,B,V,V,V,V,V,B,P,P,P,P,P,P,L,B],
    [L,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,V,V,V,V,V,B,P,P,P,P,P,P,L,B],
    [L,V,V,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,P,P,P,P,P,P,L,B],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L,B],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,B,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L,B],
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,B]]


paradinho = 0
pulando = 1
caindo = 2


class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, foto_do_azulejo, filas, colunas):
        
        pygame.sprite.Sprite.__init__(self)

        
        foto_do_azulejo = pygame.transform.scale(foto_do_azulejo, (tamanho_azulejo, tamanho_azulejo))

       
        self.image = foto_do_azulejo
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect()
        self.rect = self.image.get_rect()

        
        self.rect.x = tamanho_azulejo * colunas
        self.rect.y = tamanho_azulejo * filas



class Player(pygame.sprite.Sprite):

    def __init__(self, bonequinho, filas, colunas, piso_parede):

        
        pygame.sprite.Sprite.__init__(self)

        
        self.estado_do_jogo = paradinho

       
        bonequinho = pygame.transform.scale(bonequinho, (70, 40))

        
        self.image = bonequinho
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect()
        self.rect = self.image.get_rect()

       
        self.piso_parede = piso_parede

        
        self.rect.x = colunas * tamanho_azulejo
        self.rect.bottom = filas * tamanho_azulejo

        self.speedx = 0
        self.speedy = 0

    velocidade_no_eixo_x = 10
    
    def update(self):
        
        #self.speedy += velocidade_de_queda
        """
        if self.speedy > 0:
          self.estado_do_jogo = caindo
        """

        if self.speedy != 0 or self.speedx != 0:
            self.estado_do_jogo = caindo
        
        self.rect.y += self.speedy
        
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False, pygame.sprite.collide_mask)
        
        for colisao in colisoes:
            
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                
                self.speedy = 0
                
                #self.estado_do_jogo = paradinho
           
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                
                self.speedy = 0
                
                #self.estado_do_jogo = paradinho

       
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= largura:
            self.rect.right = largura - 1
        
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False, pygame.sprite.collide_mask)
        
        for colisao in colisoes:
            
            if self.speedx > 0:
                self.rect.right = colisao.rect.left #+largura_do_jogador/2
                self.speedx = 0
            
            elif self.speedx < 0:
                self.rect.left = colisao.rect.right 
                self.speedx = 0

    """
    def jump(self):
        
        if self.estado_do_jogo == paradinho:
            self.speedy -= quanto_pula
            self.estado_do_jogo = pulando
    """



