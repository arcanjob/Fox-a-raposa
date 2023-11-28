import pygame
import random
from os import path
from Variaveis_e_funcoes import *


pygame.init()
pygame.mixer.init()

janela = pygame.display.set_mode((largura, altura))

#ESTABELECER OS SONS

def bases_carregando(img_dir):
    assets = {}
    assets[bonequinho] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets[B] = pygame.image.load(path.join('imagens_e_sons/imagens/plataforma.png')).convert()
    assets[E] = pygame.image.load(path.join('imagens_e_sons/imagens/espinho.png')).convert_alpha()
    assets[G] = pygame.image.load(path.join('imagens_e_sons/imagens/galinha.webp')).convert_alpha()
    assets[O] = pygame.image.load(path.join('imagens_e_sons/imagens/portal.png')).convert_alpha()
    return assets


def tela_do_jogo(janela):
    pygame.mixer.music.load('imagens_e_sons/sons/som_de_fundo.mp3') #Fonte: https://youtu.be/dDOfzfifwGE?si=GfIuDBJCHU0t26uN
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    
    clock = pygame.time.Clock()
    assets = bases_carregando(0)

    todos_os_sprites= pygame.sprite.Group()
    espinhos = pygame.sprite.Group()
    piso_parede = pygame.sprite.Group()
    galinhas = pygame.sprite.Group()

    player = Player(assets[bonequinho], 12, 2, piso_parede)

    #CRIANDO O MAPA 
    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            if tile_type == B:
                tile = Tile(assets[tile_type], filas, colunas, de_peh)
                todos_os_sprites.add(tile)
                piso_parede.add(tile)
            if tile_type == EE:
                tile_type = E
                tile = Tile(assets[tile_type], filas, colunas, com_o_peh_pra_direita)
                todos_os_sprites.add(tile)
                espinhos.add(tile)
            if tile_type == ED:
                tile_type = E
                tile = Tile(assets[tile_type], filas, colunas, com_o_peh_pra_esquerda)
                todos_os_sprites.add(tile)
                espinhos.add(tile)
            if tile_type == EB:
                tile_type = E
                tile = Tile(assets[tile_type], filas, colunas, de_ponta_cabeca)
                todos_os_sprites.add(tile)
                espinhos.add(tile)
            if tile_type == G:
                tile = Tile(assets[tile_type], filas, colunas, de_peh)
                todos_os_sprites.add(tile)
                galinhas.add(tile)
            if tile_type == O:
                tile = Tile(assets[tile_type], filas, colunas, de_peh)
                todos_os_sprites.add(tile)
                galinhas.add(tile)


                
    
    todos_os_sprites.add(player)

    jogando = 0
    DONE = 1


    estado_do_jogo = jogando
    while estado_do_jogo != DONE:

        clock.tick(FPS)
    
        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                estado_do_jogo = DONE

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT and player.speedy == 0:

                    player.speedx = -velocidade_no_eixo_x
                elif event.key == pygame.K_RIGHT and player.speedy == 0:
                    player.speedx = +velocidade_no_eixo_x
                #elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                #    player.jump()
                elif event.key == pygame.K_UP and player.speedx == 0:
                    player.speedy = -velocidade_no_eixo_x
                elif event.key == pygame.K_DOWN and player.speedx == 0:
                    player.speedy = velocidade_no_eixo_x

            """
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    player.speedx += velocidade_no_eixo_x
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= velocidade_no_eixo_x
            """
        #
        todos_os_sprites.update()
        img_fundo = pygame.image.load('imagens_e_sons/imagens/Fundo_jogo.jpg').convert_alpha() #O FUNDO SERÁ UMA ANIMAÇÃO
        img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
        
        janela.blit(img_fundo, (0,0))
        todos_os_sprites.draw(janela)

        
        pygame.display.flip()





pygame.display.set_caption(TITULO)

try:
    tela_do_jogo(janela)
    #tela_do_jogo(janela)
finally:
    pygame.quit()