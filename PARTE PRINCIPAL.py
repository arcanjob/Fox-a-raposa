import pygame
pygame.init()


window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('NOSSO JOGO')

game = True


while game:
    
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
            game = False

   
    window.fill((0, 71, 171)) 
    pygame.display.update()


pygame.quit()

