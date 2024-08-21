'''
Hola este es modulo game_over,
este modulo manejara la escena cuando muere el jugador
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

#* Creamos la escena de game over
def game_over_screen(screen):
    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(40)
