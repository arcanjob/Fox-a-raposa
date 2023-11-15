
import pygame
from parametros import *
pygame.init()

window = pygame.display.set_mode((1000, 600))

#DEFININDO AS IMAGENS



#DEFININDO OS TAMANHOS DO PERSONAGEM E DOS ESPINHOS



# JANELA
JANELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('NOSSO JOGO')

#FUNDO DA IMAGEM


#SPRITE DA PLATAFORMA

















game = True


while game:
    
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
            game = False


    window.fill((0, 71, 171)) 
    pygame.display.update()


pygame.quit()

