'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy

#* Ahora gameloop recibe screen y las dimensiones de la pantalla
def gameLoop(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    ''' cargar el fondo'''
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    ''' 5- Disparos''' #*
    piu = pygame.mixer.Sound('assets/blaster.mp3') # Sonido de disparo
    
    # Cambiar el cursor por una imagen
    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load("assets/crosshair.png").convert_alpha()
    cursor_img = pygame.transform.scale(cursor_img, (35, 35))
    cursor_img_rect = cursor_img.get_rect()

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # loop principal del juego
    while running:

        screen.blit(background_image, [0, 0])
        
        for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
        
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        #* Dibuja el cursor del mouse
        cursor_img_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_img_rect)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        
        if pygame.sprite.spritecollideany(player, enemies, pygame.sprite.collide_mask):
            player.kill()
            running = False
        
        #* Si un proyectil golpea a un enemigo, el proyectil y el enemigo mueren
        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
                
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            #* Dispara un proyectil si el usuario hace click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(piu) #* Reproduce el sonido de disparo
                player.shoot(pygame.mouse.get_pos())

        clock.tick(40)
        pygame.display.flip()
