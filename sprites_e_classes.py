import pygame
pygame.init()

from parametros import *

'''
    def cooldown(self):
        agora = pygame.time.get_ticks()

        delta_pulo = agora - ultimo_pulo
        if delta_pulo > 50:
            pular(botao)
    '''

class personagem (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.rotacao = 0
        self.i = 0
        self.estado = parado
        
        self.imagem = pygame.transform.rotate(anim_parado[self.i], self.rotacao)
        self.mascara = pygame.mask.from_surface(self.imagem)
        self.rect = self.imagem.get_rect()
        
        #ESTADO INICIAL DO PERSONAGEM - POSIÇÃO E PARADO
        self.rect.centerx = x_meio_inicial_do_personagem
        self.rect.bottom = y_peh_inicial_do_personagem
        self.velocidadex = 0
        self.velocidadey = 0


    def update(self): #MOVIMENTO - VELOCIDADE À DEFINIR
        #atualizando a posição do player
        
        #MOVIMENTANDO O PERSONAGEM
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey

        #ESTÁ PARADO
        if self.velocidadex == 0 and self.velocidadey == 0:
            self.estado = parado
        if self.estado == parado:
            self.imagem = pygame.transform.rotate(anim_parado[self.i], self.rotacao)  
            self.mascara = pygame.mask.from_surface(self.imagem)
        if self.i == len(anim_parado):
            self.i = 0


        #ESTÁ PULANDO
        if self.velocidadex != 0 or self.velocidadex != 0:
            self.estado = pulando
        if self.estado == pulando:
            self.imagem = pygame.transform.rotate(anim_parado[self.i], self.rotacao) 
            self.mascara = pygame.mask.from_surface(self.imagem)
        if self.i == len(anim_pulando):
            self.i = 0
        


        #dentro da tela - desacelerando e mantendo dentro da tela - NO FUTURO, DEVO FAZER O MESMO PARA QUANDO O PERSONAGEM COLIDIR COM AS PAREDES
        if self.rect.right >= LARGURA_JANELA:
            self.velocidadex = 0
            self.rect.right = LARGURA_JANELA
        if self.rect.left <= 0:
            self.velocidadex = 0
            self.rect.left = 0
        if self.rect.top <= 0:
            self.velocidadey = 0
            self.rect.top = 0
        if self.rect.bottom >= ALTURA_JANELA:
            self.rect.bottom = ALTURA_JANELA
            self.velocidadey = 0



class objeto:
    def __init__(self, fila, coluna, imagem, rotacao):
        self.imagem = pygame.transform.rotate(imagem)

        self.rect = self.imagem.get_rect()
        
        self.rect.x = fila
        self.rect.y = coluna
        x_original = fila
        y_original = coluna





class morrendo(pygame.sprite.Sprite):
    # Construtor da classe.
    #def __init__(self, center):


#SPRITE  - MORRENDO
class sprite_morrendo(pygame.sprite.Sprite):   #Código inspirado no handout do pygame presente na academia python
    def __init__(self, centro):

        pygame.sprite.Sprite.__init__(self)

        # ATUALIZANDO A ANIMAÇÃO DO PERSONAGEM MORRENDO
        self.anim_morrendo = anim_morrendo

        
        self.frame = 0  #NUMERANDO O PRIMEIRO FRAME - SE ATUALIZARÁ
        self.imagem = pygame.transform.rotate(self.anim_morrendo[self.i], self.rotacao)   #SELECIONANDO O ARQUIVO DA ANIMAÇÃO CORRESPONDENTE AO FRAME E
        #ACRESCENTANDO A ROTACAO
        
        #ATUALIZANDO A POSIÇÃO
        self.rect = self.image.get_rect()
        self.rect.centro = centro # O CENTRO SERÁ DADO QUANDO A CLASSE FOR EVOCADO
        
        
        self.ultimo_update = pygame.time.get_ticks() #QUANDO A PRIMEIRA IMAGEM FOI MOSTRADA

        self.espera = 50 #AGUARDO ENTRE UM FRAME E O PRÓXIMO


    def update(self):
        # Verifica o tick atual.
        agora = pygame.time.get_ticks()
        #### now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        
        tempo_decorrido = agora - self.ultimo_update

        # Se já está na hora de mudar de imagem...
        if tempo_decorrido > self.espera:
            # Marca o tick da nova imagem.
            self.ultimo_update = agora
            #### self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            """
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            """
            if self.frame == len(self.anim_morrendo):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                centro = self.rect.centro
                self.imagem = self.anim_morrendo[self.frame] #self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.centro = centro

