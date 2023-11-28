import pygame
import random
from os import path

jogando = 0
DONE = 1
inicio = 3

def tela_do_jogo(janela):
    
    clock = pygame.time.Clock()
    assets = bases_carregando(img_dir)

    todos_os_sprites= pygame.sprite.Group()
    
    piso_parede = pygame.sprite.Group()

    player = Player(assets[bonequinho], 12, 2, piso_parede)

    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            if tile_type == B:
                tile = Tile(assets[tile_type], filas, colunas)
                todos_os_sprites.add(tile)
                piso_parede.add(tile)

img_dir = path.join(path.dirname(__file__), 'imagens_e_sons')
def bases_carregando(img_dir):
    assets = {}
    assets[bonequinho] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets[B] = pygame.image.load(path.join('imagens_e_sons/imagens/plataforma.png')).convert()
    assets["sons"] = []
    return assets

def tela_inicial(JANELA):

    
    pygame.mixer.music.play(loops=-1)
    # Carrega o fundo da tela inicial
    estado_do_jogo = jogando
    while estado_do_jogo == inicio:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)                                                            #CHAMA O FPS - FEITO

        # Processa os eventos (mouse, teclado, botão, etc).
        for evento in pygame.event.get():
            # Verifica se foi fechado.
            if evento.type == pygame.QUIT:
                pygame.quit()
            #0 = game over, congrats;   1 - fecha; 2,3,5 - congrats, 4 - nao fecha 
            if evento.type == pygame.KEYUP:
                estado_do_jogo = jogando

        # A cada loop, redesenha o fundo e os sprites
        JANELA.blit(img_inicio, (0, 0)) #imagem com o escrito "para recomeçar, pressione qualquer tecla"             - CHAMA A IMG_INICIO - FEITO


        # Depois de desenhar tudo, inverte o display.??????
        pygame.display.flip() 

    return estado_do_jogo


def tela_do_jogo(janela):
    
    clock = pygame.time.Clock()

    
    assets = bases_carregando(img_dir)

    
    all_sprites = pygame.sprite.Group()
    
    piso_parede = pygame.sprite.Group()

    
    player = Player(assets[bonequinho], 12, 2, piso_parede)

    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            if tile_type == B:
                tile = Tile(assets[tile_type], filas, colunas)
                all_sprites.add(tile)
                piso_parede.add(tile)

    
    all_sprites.add(player)

    jogando = 0
    DONE = 1

    estado_do_jogo = jogando
 
def tela_do_jogo(janela):
    
    clock = pygame.time.Clock()

    assets = bases_carregando(img_dir)

    all_sprites = pygame.sprite.Group()
    
    piso_parede = pygame.sprite.Group()
    
    player = Player(assets[bonequinho], 12, 2, piso_parede)

    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            if tile_type == B:
                tile = Tile(assets[tile_type], filas, colunas)
                all_sprites.add(tile)
                piso_parede.add(tile)

    
    all_sprites.add(player)

    jogando = 0
    DONE = 1

    estado_do_jogo = jogando

TITULO = 'Fox, a raposa'
largura = 1350
altura = 680 
tamanho_azulejo = 40
largura_do_jogador = tamanho_azulejo + 5 
altura_do_jogador = int(tamanho_azulejo * 1.5)
FPS = 60


bonequinho = 'moeda_img'

BLACK = (0, 0, 0)

velocidade_de_queda = 5

quanto_pula = tamanho_azulejo

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
       
        self.rect = self.image.get_rect()

        
        self.rect.x = tamanho_azulejo * colunas
        self.rect.y = tamanho_azulejo * filas



class Player(pygame.sprite.Sprite):

    def __init__(self, bonequinho, filas, colunas, piso_parede):

        
        pygame.sprite.Sprite.__init__(self)

        
        self.estado_do_jogo = paradinho

       
        bonequinho = pygame.transform.scale(bonequinho, (largura_do_jogador, altura_do_jogador))

        
        self.image = bonequinho
        
        
        self.rect = self.image.get_rect()

       
        self.piso_parede = piso_parede

        
        self.rect.x = colunas * tamanho_azulejo
        self.rect.bottom = filas * tamanho_azulejo

        self.speedx = 0
        self.speedy = 0

    velocidade_no_eixo_x = 10
    def update(self):
        
        self.speedy += velocidade_de_queda
        
        if self.speedy > 0:
            self.estado_do_jogo = caindo
        
        self.rect.y += self.speedy
        
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False)
        
        for colisao in colisoes:
            
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                
                self.speedy = 0
                
                self.estado_do_jogo = paradinho
           
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                
                self.speedy = 0
                
                self.estado_do_jogo = paradinho

       
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= largura:
            self.rect.right = largura - 1
        
        colisoes = pygame.sprite.spritecollide(self, self.piso_parede, False)
        
        for colisao in colisoes:
            
            if self.speedx > 0:
                self.rect.right = colisao.rect.left
            
            elif self.speedx < 0:
                self.rect.left = colisao.rect.right

    
    def jump(self):
        
        if self.estado_do_jogo == paradinho:
            self.speedy -= quanto_pula
            self.estado_do_jogo = pulando



