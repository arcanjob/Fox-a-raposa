import pygame
from parametros import *

from sprites_e_classes import *




###########################################################JOGO#################################################


def jogando(JANELA):
    cronometro = pygame.time.Clock()

    personagem = personagem()
    
    if FASE == 1:
    F = F1
    elif FASE == 2:
        F = F2
    elif FASE == 3:
        F = F3
    
    F['all_sprites'].add(personagem)

    F['vidas'] = 3



    GAME_OVER  = 0
    JOGANDO = 1
    MORRENDO = 2
    DONE = 3
    INICIO = 4
    VITORIA = 5



    keys_down = {}

    pygame.mixer.som_fundo.play(loops=-1)
    estado_do_jogo = JOGANDO
    
    while estado_do_jogo == JOGANDO:
        clock.tick(FPS)



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
                    if event.key == pygame.K_LEFT or event.key == pygame.K_d and personagem.velocidadey == 0 :
                        personagem.velocidadex -= 8
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_a and personagem.velocidadey == 0 :
                        personagem.velocidadex += 8
                    if event.key == pygame.K_UP or event.key == pygame.K_w and personagem.velocidadex == 0 :
                        personagem.velocidadey -= 8
                    if event.key == pygame.DOWN or event.key == pygame.K_s and personagem.velocidadex == 0 :
                        personagem.velocidadey +=8


        #ROTACIONANDO EM RELAÇÃO AO SEU MOVIMENTO - ***CALIBRAR A VELO DISSO
        if personagem.velocidadey>0 and personagem.rotacao != 180:
            personagem.rotacao += velocidade_de_rotaca_p_frame
        if personagem.velocidadey<0 and personagem.rotacao != 0:
            personagem.rotacao -= velocidade_de_rotaca_p_frame
        if personagem.velocidadex >0 and personagem.rotacao != 270:
            personagem.rotacao +=velocidade_de_rotaca_p_frame
        if personagem.velocidadex<1 and personagem.rotacao != 90:
            personagem.rotacao -= velocidade_de_rotaca_p_frame

        
        all_sprites.update()


        if estado_do_jogo == JOGANDO:

            #RESPONDENDO ÀS COLISÕES COM AS PLATAFORMAS
            colisoes_plataformas = pygame.sprite.spritecollide(personagem, F1['plataformas'], False, pygame.sprite.collide_mask)
            if colisoes_plataformas:
                if personagem.velocidadex !=0:
                    personagem.velocidadex -= personagem.velocidadex  # para o jogador
                elif personagem.velocidadey !=0:
                    personagem.velocidadey -= personagem.velocidadey  # para o jogador
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
                morte = morrendo(personagem.rect.center)

                all_sprites.add(morte)
                keys_down = {}
                estado_do_jogo = MORRENDO
                hora_da_morte = pygame.time.Clock()
                duracao_da_morte = t_dos_frames_de_morte*len(morte.anim_da_morte) + 400

            
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

