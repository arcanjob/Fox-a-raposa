import pygame
import random
from os import path
from Variaveis_e_funcoes import * 

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



pygame.init()
pygame.mixer.init()


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