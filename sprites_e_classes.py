from parametros import *

class personagem (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = img_personagem
        self.mascara = pygame.mask.from_surface(self.imagem)
        self.rect = self.imagem.get_rect()
        
        #ESTADO INICIAL DO PERSONAGEM - POSIÇÃO E PARADO
        self.rect.centerx = x_meio_ininicial_do_personagem
        self.rect.bottom = y_peh_inicial_do_personagem
        self.velocidadex = 0
        self.velocidadey = 0


    def update(self): #MOVIMENTO - VELOCIDADE À DEFINIR
        #atualizando a posição do player
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey

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
    '''
    def cooldown(self):
        agora = pygame.time.get_ticks()

        delta_pulo = agora - ultimo_pulo
        if delta_pulo > 50:
            pular(botao)
    '''

class plataforma (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = img_plataformas
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


