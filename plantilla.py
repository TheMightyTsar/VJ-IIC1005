import pygame
import random

from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL)

'''----- aqui puedes definir los Objetos--------'''
### BUGpng = pygame.image.load('bug.png')
### BUGpng_scaled = pygame.transform.scale(image1_not_scaled, (64, 64))

BUGpng = None
BUGpng_scaled = None

### JorgePNG= pygame.image.load('JorgeVJ.png')
### JorgePNG_scaled = pygame.transform.scale(imageNotScaled, (80, 80))
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


'''-- hasta aqui puedes añadir los Objetos-----'''

''' iniciamos los modulos de pygame'''

pygame.init()

''' Creamos y editamos la ventana de pygame (escena) '''
''' 1.-definir el tamaño de la ventana'''
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

''' 2.- crear el objeto pantalla'''
### screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = None
### background_image = pygame.image.load("pixelBackground.jpg").convert()
background_image = None


''' Preparamos el gameloop '''
''' 1.- creamos el reloj del juego'''
### clock = pygame.time.Clock()  --> clase interna pygame
clock = None
''' 2.- generador de enemigos'''
### ADDENEMY = pygame.USEREVENT + 1  --> Mecanicas internas de pygame (tiene X cantidad de eventos disponibles)
ADDENEMY = None
### pygame.time.set_timer(ADDENEMY, 350) --> cada 350 TICKS

''' 3.- creamos la instancia de jugador'''
### player = Player()  --> al principio no hay imagenes

''' 4.- contenedores de enemigos y jugador'''
### enemies = pygame.sprite.Group()
### all_sprites = pygame.sprite.Group()
### all_sprites.add(player)

''' hora de hacer el gameloop '''
### runing = True

### while running:
# iteramos sobre cada evento en la cola
### 	for event in pygame.event.get():
# se presiono una tecla?
### 		if event.type == KEYDOWN:
# era la tecla de escape? -> entonces terminamos
### 			if event.key == K_ESCAPE:
### 				running = False

# fue un click al cierre de la ventana? -> entonces terminamos
### 		elif event.type == QUIT:
### 			running = False

# es un evento que agrega enemigos?
### 		elif event.type == ADDENEMY:
### 			new_enemy = Enemy()
### 			enemies.add(new_enemy)
### 			all_sprites.add(new_enemy)

### 	screen.blit(background_image, [0, 0])


# dibujamos todos los sprites
### 	for entity in all_sprites:
### 		screen.blit(entity.surf, entity.rect)

# vemos si algun enemigo a chocado con el jugador
### 	if pygame.sprite.spritecollideany(player, enemies):
# si pasa, removemos al jugador y detenemos el loop del juego
### 		player.kill()
### 		running = False

# actualizamos la interfaz
### 	pygame.display.flip()

### 	clock.tick(60)

# obtenemos todas las teclas presionadas actualmente
### 	pressed_keys = pygame.key.get_pressed()

# actualizamos el sprite del jugador basado en las teclas presionadas
### 	player.update(pressed_keys)

# obtenemos todas las teclas presionadas actualmente
### 	pressed_keys = pygame.key.get_pressed()

# actualizamos el sprite del jugador basado en las teclas presionadas
### 	player.update(pressed_keys)

# actualizamos los enemigos
###     	enemies.update()
