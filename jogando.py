import pygame
import os
from mapa import *
from parametros import *
from math import *
from sprites_e_classes import *


###########################################################JOGO#################################################

def jogando(JANELA):
    cronometro = pygame.time.Clock()
    personagem.i = 0
    personagem = personagem()
    
    if FASE == 1:
        F = F1
        mapa = MAPA_1
    elif FASE == 2:
        F = F2
        mapa = MAPA_2
    elif FASE == 3:
        F = F3
        mapa = MAPA3
    
    GAME_OVER  = 0
    JOGANDO = 1
    MORRENDO = 2
    DONE = 3
    INICIO = 4
    VITORIA = 5

    keys_down = {}

    pygame.mixer.som_fundo.play(loops=-1)
    estado_do_jogo = JOGANDO
    
    for fila in range(len(mapa)):
            for coluna in range(len(mapa[fila])):
                tile_type = mapa[fila][coluna]
                if tile_type == BLOCK:
                    tile = Tile(assets[tile_type], row, column)
                    all_sprites.add(tile)
                    blocks.add(tile)
   
    F['all_sprites'].add(personagem)

    F['vidas'] = 3


    while estado_do_jogo == JOGANDO:
        clock.tick(FPS)


        personagem.i +=1
        #EVENTOS

        for event in pygame.event.get():
            #APERTOU NO X DE SAIR:
            if event.type == pygame.QUIT:
                estado_do_jogo = DONE
            
            #MOVIMENTANDO O PERSONAGEM
            if estado_do_jogo == JOGANDO:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # DEPENDENDO DA TECLA E SE ALGUM OUTRO MOVIMENTO JÁ ESTÁ ACONTECENDO
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a and personagem.velocidadey == 0 :
                        personagem.velocidadex -= 8
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d and personagem.velocidadey == 0 :
                        personagem.velocidadex += 8
                    if event.key == pygame.K_UP or event.key == pygame.K_w and personagem.velocidadex == 0 :
                        personagem.velocidadey -= 8
                    if event.key == pygame.DOWN or event.key == pygame.K_s and personagem.velocidadex == 0 :
                        personagem.velocidadey +=8


        #ROTACIONANDO EM RELAÇÃO AO SEU MOVIMENTO - ***CALIBRAR A VELO DISSO
        if personagem.velocidadey>0 and personagem.orientacao != de_peh:
            personagem.orientacao += velocidade_de_rotaca_p_frame
        if personagem.velocidadey<0 and personagem.orientacao != de_ponta_cabeca:
            personagem.orientacao -= velocidade_de_rotaca_p_frame
        if personagem.velocidadex >0 and personagem.orientacao != virado_para_a_direita:
            personagem.orientacao +=velocidade_de_rotaca_p_frame
        if personagem.velocidadex<0 and personagem.orientacao != virado_para_a_esquerda:
            personagem.orientacao -= velocidade_de_rotaca_p_frame

        
        F['all_sprites'].update()


        if estado_do_jogo == JOGANDO:

            #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
            colisoes_plataformas = pygame.sprite.spritecollide(personagem, F1['plataformas'], False, pygame.sprite.collide_mask)
            if colisoes_plataformas:
                if personagem.velocidadex !=0:
                    personagem.velocidadex = 0  # para o jogador
                elif personagem.velocidadey !=0:
                    personagem.velocidadey = 0  # para o jogador
                som_caido.play()

            #COLISOES COM MOEDAS
            colisoes_moedas = pygame.sprite.spritecollide(personagem, F['moedas'], True, pygame.sprite.collide_mask)
            if colisoes_moedas:
                pontos+=50
                som_pegando_moedas.play()
        

            #COLISÃO COM OS ESPINHOS
            colisoes_espinhos = pygame.sprite.spritecollide(personagem, F['espinhos'], False, pygame.sprite.collide_mask)
            if colisoes_espinhos:        
                som_morrendo.play()
                personagem.kill()
                vidas -= 1
                morte = sprite_morrendo(personagem.rect.center)

                F['all_sprites'].add(morte)
                keys_down = {}
                estado_do_jogo = MORRENDO
                hora_da_morte = pygame.time.Clock()
                duracao_da_morte = morrendo.espera * len(morrendo.anim_morrendo) + 400

            
            #COLISAO COM A CHEGADA
            colisao_chegada = pygame.sprite.spritecollide(personagem, F['chegada'], False, pygame.sprite.collide_mask)
            if colisao_chegada:
                som_vitoria.play()
                estado_do_jogo = VITORIA


        elif estado_do_jogo == MORRENDO:
            agora = pygame.time.get_ticks()

            if agora - hora_da_morte > duracao_da_morte:
                if vidas == 0:
                    estado_do_jogo = GAME_OVER   #A PESSOA MORREU
                else: 
                    estado_do_jogo = JOGANDO
                    personagem = personagem()
                    F['vidas']-=1
                    F['all_sprites'].add(personagem)

                    resetar_moedas(F['moedas'])


        #GERANDO SAIDAS
        JANELA.fill(PRETO)
        JANELA.blit(img_fundo,(0,0))

        F['all_sprites'].draw(JANELA)

        #PONTUAÇÃO
        perfil_texto = fonte_pontos.render("{:08d}".format(pontos), True, AMARELO)
        texto_rect = perfil_texto.get_rect()
        texto_rect.midtop = (LARGURA_JANELA / 2,  10)
        JANELA.blit(perfil_texto, texto_rect)

        #VIDAS
        perfil_texto = fonte_pontos.render(chr(9829) * vidas, True, VERMELHO)
        texto_rect = perfil_texto.get_rect()
        texto_rect.bottomleft = (10, ALTURA_JANELA - 10)
        JANELA.blit(perfil_texto, texto_rect)


        pygame.display.update()
        return estado_do_jogo

