import pygame
import random
from os import path
from variaveis_e_funcoes import *


pygame.init()
pygame.mixer.init()

#ESTABELECER OS SONS
pygame.mixer.music.load('imagens_e_sons/sons/som_de_fundo.mp3') #Fonte: https://youtu.be/dDOfzfifwGE?si=GfIuDBJCHU0t26uN
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

def load_assets(img_dir):
    assets = {}
    assets[bonequinho] = pygame.image.load(path.join('imagens_e_sons/imagens/Walk_(1).png')).convert_alpha()
    assets[B] = pygame.image.load(path.join('imagens_e_sons/imagens/plataforma.png')).convert()
    return assets


def game_screen(janela):
    
    clock = pygame.time.Clock()

    
    assets = load_assets(img_dir)

    
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

    PLAYING = 0
    DONE = 1

    estado_do_jogo = PLAYING
    estado_do_jogo = PLAYING
    while estado_do_jogo != DONE:

        
        clock.tick(FPS)

        
        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                estado_do_jogo = DONE

            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

        #
        all_sprites.update()
        img_fundo = pygame.image.load('imagens_e_sons/imagens/Fundo_jogo.jpg').convert_alpha() #O FUNDO SERÁ UMA ANIMAÇÃO
        img_plataformas = pygame.image.load('imagens_e_sons/imagens/plataforma.png').convert_alpha()
        
        janela.blit(img_fundo, (0,0))
        all_sprites.draw(janela)

        
        pygame.display.flip()






janela = pygame.display.set_mode((largura, altura))


pygame.display.set_caption(TITULO)


print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')


try:
    game_screen(janela)
finally:
    pygame.quit()