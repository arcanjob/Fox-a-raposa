
#Chama todas as bibliotécas que serão usadas ao longo de todo o código
import pygame
import random
from os import path

#inicializa  o pygame
pygame.init()
#inicializa  o pygame mixer (parte que controla o som)
pygame.mixer.init()
pygame.init()
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
largura = 1360
altura = 680 

#Define o tamanho dos azulejos do jogo (o piso)
tamanho_azulejo = 40

#define o tamanho do jogador, a nossa raposa, com relação ao tamanho do azulejo
largura_do_jogador = tamanho_azulejo
altura_do_jogador = int(tamanho_azulejo * 1)

#Define a taxa de frames do jogo
FPS = 60

#Define a cor preta
preto = (0, 0, 0)
branco = (255,255,255)
vermelho = (200, 100, 100)
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
MAPA = [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,O,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,G,V,V,V,V,V,V,B,B],
    [ED,V,V,V,V,G,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B,B],
    [B,V,V,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,V,V,R,V,V,V,V,V,V,V,V,V,V,V,G,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]


#Variáveis que irão ser usada para definir o estado do jogador
paradinho = 0
pulando = 1
caindo = 2


#Estabelece as imagens a serem usadas


def bases_carregando(none):
    assets = {}
    assets[bonequinho] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets["img_fundo"] = pygame.image.load('imagens_e_sons/imagens/Fundo_jogo.jpg').convert_alpha() 
    assets["plataformas"] = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
    assets[B] = pygame.image.load(path.join('imagens_e_sons/imagens/plataforma.png')).convert()
    assets[E] = pygame.image.load(path.join('imagens_e_sons/imagens/espinho.png')).convert_alpha()
    assets[G] = pygame.image.load(path.join('imagens_e_sons/imagens/galinha.webp')).convert_alpha()
    assets[O] = pygame.image.load(path.join('imagens_e_sons/imagens/portal.png')).convert_alpha()
    assets[R] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets["fonte_dos_pontos"] = pygame.font.Font('imagens_e_sons/imagens/PressStart2P.ttf', 28)
    return assets



#Cria a função 
class azulejo(pygame.sprite.Sprite):

    # Constrói a classe
    def __init__(self, foto_do_azulejo, filas, colunas):
        
        pygame.sprite.Sprite.__init__(self)

        #adicona a foto do azulejo a uma variável
        foto_do_azulejo = pygame.transform.scale(foto_do_azulejo, (tamanho_azulejo, tamanho_azulejo))

vidas = 3


pode_passar = 200000000000000000000000
#Cuida do estado de jogo
jogando = 0
DONE = 1
morreu_de_vez = 2
morreu = 3
vitoria = 4
sim = 5
vivo = 6
INICIO = 7
#Marca o loop principal em que o jogo irá funcionar

estado_do_jogador = vivo

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






#fUNÇÃO QUE VAI EXIBIR O TEXTO INICIAL PARA O USÚÁRIO
def tela_inicial_de_texto(janela):
    frases_para_serem_exibidas = [
    'Você está prestes a jogar um incìrivel jogo',
    'Há poucas regras para se atentar',
    'uepa!!!', 'para se mover basta clicar nas setinhas do teclado', 'para passar, você precisará pegar todas as galinhas' ]

    #Define a fonte do texto que será usada
    font = pygame.font.SysFont(None, 45)

    #inicializa o indice do texto para que ele seja percorrido
    indice_do_textoo = 0

    #loop principal da tela de inicio, em que será rodado e exibido os textos
    while indice_do_textoo < len(frases_para_serem_exibidas):

        #usa o tmepo de acordo com a taxa de FPS determinada previamente
        clock.tick(FPS)

        #para cada evento ele vai ficar conferindo e vendo o que há para fazer dentro dos "IFs"
        for evento in pygame.event.get():
            
            #Determina quando tem que sair dessa tela


            if evento.type == pygame.QUIT:
                pygame.quit()

            #Verifica o fenomeno de apertar uma tecla
            if evento.type == pygame.KEYDOWN:
                indice_do_textoo += 1
                    print('ta ino')
                #coonfere se a tecla pressionada era o espaço
                #if evento.key == pygame.K_SPACE or evento.key == pygame.K_DOWN:
                    

        
        if indice_do_textoo < len(frases_para_serem_exibidas):
            texto = frases_para_serem_exibidas[indice_do_textoo]
        else:
            texto = ''
        texto_image = font.render(texto, True, branco)
        img_fundo = pygame.image.load('imagens_e_sons/imagens/inicio.png').convert_alpha()
        img_fundo = pygame.transform.scale(img_fundo, (largura, altura)) 
        janela.blit(img_fundo, (0,0))
   
        #define em que posição o texto irá ser gerado
        janela.blit(texto_image, (375, 550))
        pygame.display.flip()

        #print('to preso')
    print('to quase')
    return jogando

def tela_de_derrota(janela):
    frase_para_derrota = ["Infelizmente você morreu, aperte espaço para continuar"]
    #Define a fonte do texto que será usada
    font = pygame.font.SysFont(None, 45)

    #inicializa o indice do texto para que ele seja percorrido
    indice_do_texto = 0

    #loop principal da tela de inicio, em que será rodado e exibido os textos
    while indice_do_texto < len(frase_para_derrota):

        #usa o tmepo de acordo com a taxa de FPS determinada previamente
        clock.tick(FPS)

        #para cada evento ele vai ficar conferindo e vendo o que há para fazer dentro dos "IFs"
        for evento in pygame.event.get():
            
            #Determina quando tem que sair dessa tela
            if evento.type == pygame.QUIT:
                pygame.quit()

            #Verifica o fenomeno de apertar uma tecla
            if evento.type == pygame.KEYDOWN:

                #coonfere se a tecla pressionada era o espaço
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_DOWN:
                    indice_do_texto += 1

        
        if indice_do_texto < len(frase_para_derrota):
            texto = frase_para_derrota[indice_do_texto]
        else:
            texto = ''
        texto_image = font.render(texto, True, branco)
        img_fim = pygame.image.load('imagens_e_sons/imagens/fim.png').convert_alpha()    #tela do game over
        img_fim =  pygame.transform.scale(img_fim, (largura, altura)) #tela final
        janela.blit(img_fim, (0,0))
   
        #define em que posição o texto irá ser gerado
        janela.blit(texto_image, (375, 550))
        pygame.display.flip()

    return jogando

def tela_de_vitoria(janela):
    frase_para_derrota = ['''
                                MEUS PARABÉNS 
                          você ganhou essa partida!!!
                          ''']
    #Define a fonte do texto que será usada
    font = pygame.font.SysFont(None, 50)

    #inicializa o indice do texto para que ele seja percorrido
    indice_do_texto = 0

    #loop principal da tela de inicio, em que será rodado e exibido os textos
    while indice_do_texto < len(frase_para_derrota):

        #usa o tmepo de acordo com a taxa de FPS determinada previamente
        clock.tick(FPS)

        #para cada evento ele vai ficar conferindo e vendo o que há para fazer dentro dos "IFs"
        for evento in pygame.event.get():
            
            #Determina quando tem que sair dessa tela
            if evento.type == pygame.QUIT:
                pygame.quit()

            #Verifica o fenomeno de apertar uma tecla
            if evento.type == pygame.KEYDOWN:

                #coonfere se a tecla pressionada era o espaço
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_DOWN:
                    indice_do_texto += 1

        
        if indice_do_texto < len(frase_para_derrota):
            texto = frase_para_derrota[indice_do_texto]
        else:
            texto = ''
        texto_image = font.render(texto, True, branco)
        img_fundo = pygame.image.load('imagens_e_sons/imagens/Fundo_jogo.jpg').convert_alpha() 
        img_fundo =  pygame.transform.scale(img_fundo, (largura, altura)) #tela final
        janela.blit(img_fundo, (0,0))
   
        #define em que posição o texto irá ser gerado
        janela.blit(texto_image, (375, 550))
        pygame.display.flip()

    return jogando
