
#Chama todas as bibliotécas que serão usadas ao longo de todo o código
import pygame
import random
from os import path
from Variaveis_e_funcoes import *

#inicializa  o pygame
pygame.init()
#inicializa  o pygame mixer (parte que controla o som)
pygame.mixer.init()

#Define e cria a variável em que o jogo irágirar em torno
janela = pygame.display.set_mode((largura, altura))

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
    return assets


#Define a tela do jogo e como ela irá funcionar
def tela_do_jogo(janela):
    pygame.mixer.music.load('imagens_e_sons/sons/som_de_fundo.mp3') #Fonte: https://youtu.be/dDOfzfifwGE?si=GfIuDBJCHU0t26uN
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    
    #define e usa o tempo no jogo
    clock = pygame.time.Clock()
    assets = bases_carregando(0)

    
    #define os grupos de sprites nas suas respectivas variáveis, isso será usado ao longo de todo o código
    todos_os_sprites= pygame.sprite.Group()
    espinhos = pygame.sprite.Group()
    piso_parede = pygame.sprite.Group()
    galinhas = pygame.sprite.Group()



    #Cria o mapa usando um laço de rpetição (FOR) para ler a nossa lista de listas que define o mapa em si 
    for filas in range(len(MAPA)):
        for colunas in range(len(MAPA[filas])):
            tile_type = MAPA[filas][colunas]
            
            #Confere cada letra dentro do dito mapa para atribuir uma carácteristica a ela e uma imagem
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
            if tile_type == R:
                y = filas
                x = colunas

    #Define onde o jogador irá ser invocado e inicializado dentro do mapa, nesse caso, pela variável "R"
    player = Player(assets[R], y, x, piso_parede)
                
    #Adiciona o player por último para que ele fique desenhado por cima de todos os outros sprites
    todos_os_sprites.add(player)
    
    #marca o inicio da variavel de ponto
    pontos = 0

    #Cuida do estado de jogo
    jogando = 0
    DONE = 1

    #Marca o loop principal em que o jogo irá funcionar
    estado_do_jogo = jogando
    


    while estado_do_jogo != DONE:
        
        #marca o tempo
        clock.tick(FPS)
    
        

        #COLISAO COM AS GALINHAS
        colisoes = pygame.sprite.spritecollide(player, galinhas, True, pygame.sprite.collide_mask)

        for colisao in colisoes:
            pontos +=1
            print(pontos)



        # Verifica os eventos dentro do jogo
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                estado_do_jogo = DONE

            #Confere quando jogador solta uma tecla (após pressionar ela)
            if event.type == pygame.KEYDOWN:

                #confere cada tecla de movimento
                if event.key == pygame.K_LEFT and player.speedy == 0 and player.speedx == 0:
                    player.speedx = -velocidade_no_eixo_x
                elif event.key == pygame.K_RIGHT and player.speedy == 0 and player.speedx == 0:
                    player.speedx = +velocidade_no_eixo_x
                elif event.key == pygame.K_UP and player.speedx == 0 and player.speedy == 0 :
                    player.speedy = -velocidade_no_eixo_x
                elif event.key == pygame.K_DOWN and player.speedx==0  and player.speedy == 0 :
                    player.speedy = velocidade_no_eixo_x

        #Atualiza o grupo com todos os sprites
        todos_os_sprites.update()
        
        #Define a imagem de fundo
        img_fundo = assets["img_fundo"]
        img_plataformas = assets["plataformas"]
        
        janela.blit(img_fundo, (0,0))
        todos_os_sprites.draw(janela)

        
        pygame.display.flip()


pygame.display.set_caption(TITULO)

try:
    tela_do_jogo(janela)
finally:
    pygame.quit()