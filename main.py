import pygame
import random

from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL)

BUGpng = None
BUGpng_scaled = None

JorgePNG = None
JorgePNG_scaled = None


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        pass

    def update(self):
        pass


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        pass

    def update(self):
        pass


''' iniciamos los modulos de pygame'''

pygame.init()

''' Creamos y editamos la ventana de pygame (escena) '''
''' 1.-definir el tamaño de la ventana'''
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

''' 2.- crear el objeto pantalla'''
screen = None
background_image = None

''' Preparamos el gameloop '''
''' 1.- creamos el reloj del juego'''

clock = None
''' 2.- generador de enemigos'''

ADDENEMY = None

''' 3.- creamos la instancia de jugador'''

''' 4.- contenedores de enemigos y jugador'''

''' hora de hacer el gameloop '''
