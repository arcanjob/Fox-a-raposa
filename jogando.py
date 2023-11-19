import pygame
from parametros import *

from sprites_e_classes import *


#OBSTACULOS - ISSO PODE INCLUIR PAREDES E OUTROS
obstaculos= pygame.sprite.Group() 

#PLATAFORMAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
plataformas = pygame.sprite.Group()
plataforma1 = obstaculo(100, 400, img_plataformas)

plataformas.add(plataforma1)

obstaculos.add(plataformas)

#ESPINHOS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR)
espinhos = pygame.sprite.Group()
espinho1 = obstaculo(200,300, img_espinhos)
espinhos.add(espinho1)

obstaculos.add(espinhos)


#MOEDAS - POSIÇÕES E IMAGEM (E TAMANHO) A DEFINIR
moedas = pygame.sprite.Group()


moeda1 = obstaculo(23,12, img_moeda)
moedas.add(moeda1)
###############################


# Função para reposicionar as moedas
def resetar_moedas(moedas):
    for moeda in moedas:
        moeda.rect.x = moeda.x_original
        moeda.rect.y = moeda.y_original

all_sprites = pygame.sprite.Group()

all_sprites.add(obstaculos, moedas)


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


        #SE PARADO, ANIMAÇÃO DELE PARADO
        if personagem.velocidadex == 0 and personagem.velocidadey == 0:
            


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
                    estado_do_jogo = JOGANDO
                    personagem = personagem()
                    all_sprites.add(personagem)

                    resetar_moedas(moedas)
                    



        #COLISÃO COM MOEDAS
        colisoes_moedas = pygame.sprite.spritecollide(personagem, moedas, True, pygame.sprite.collide_mask)
        if colisoes_moedas:
            pontos+=50

        plataformas.draw(screen) 

