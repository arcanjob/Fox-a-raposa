import pygame
from parametros import *

from sprites_e_classes import *


#OBSTACULOS - ISSO PODE INCLUIR PAREDES E OUTROS
obstaculos= pygame.sprite.Group() 

#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
plataformas = pygame.sprite.Group()
plataformas.add(obstaculo(100, 400, img_plataformas))


obstaculos.add(plataformas)

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
espinhos = pygame.sprite.Group()
espinhos.add(obstaculo(200,300, img_espinhos))


obstaculos.add(espinhos)



all_sprites = pygame.sprite.Group()

all_sprites.add(obstaculos)

def jogando(JANELA):
    cronometro = pygame.time.Clock()

    personagem = personagem()
    all_sprites.add(personagem)

    vidas = 3
    pontos = 0


    DONE = 0
    JOGANDO = 1
    MORRENDO = 2

    keys_down = {}

    pygame.mixer.som_fundo.play(loops=-1)
    estado_do_jogo = JOGANDO
    
    while estado_do_jogo == JOGANDO:
        clock.tick(FPS)






        #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
        colisoes_plataformas = pygame.sprite.spritecollide(personagem, plataformas, False, pygame.sprite.collide_mask)

        #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
        if colisoes_plataformas:
            if personagem.velocidadex !=0:
                personagem.velocidadex -= personagem.velocidadex  # para o jogador
            elif personagem.velocidadey !=0:
                personagem.velocidadey -= personagem.velocidadey  # para o jogador


        #COLISÃO COM OS ESPINHOS
        colisoes_espinhos = pygame.sprite.spritecollide(personagem, espinhos, False, pygame.sprite.collide_mask)
        if colisoes_espinhos:           ###################
            som_dano.play()
            personagem.kill()
            vidas -= 1
            morte = morrendo(personagem.rect.center)

            all_sprites.add(morte)
            keys_down = {}
            hora_da_morte = pygame.time.Clock()
            duracao_da_morte = t_dos_frames_de_morte*len(morte.anim_da_morte) + 400

            agora = pygame.time.get_ticks()

            if agora - hora_da_morte > duracao_da_morte:
                if vidas == 0:
                    estado_do_jogo = DONE
                else: 
                    estado_do_jogo = PLAYING
                    personagem = personagem()
                    all_sprites.add(personagem)


        #COLISÃO COM MOEDAS



        plataformas.draw(screen) 

