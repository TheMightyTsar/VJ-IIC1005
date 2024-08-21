"""
Hola este es modulo principal,
el codigo que al ejecutar pondra en marcha nuestro juego
"""
import pygame
import scenes.game as GameScene
import scenes.game_over as GameOverScene

#* Inicializamos los modulos de pygame, pantalla y escenas acá
''' iniciamos los modulos de pygame'''
pygame.init()
pygame.mixer.init()

''' Creamos y editamos la ventana de pygame (escena) '''
''' 1.-definir el tamaño de la ventana'''
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

''' 2.- crear el objeto pantalla'''
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''Inicio la escena de mi juego'''
GameScene.gameLoop(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
'''Inicio la escena de game over'''
GameOverScene.game_over_screen(screen)

