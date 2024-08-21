import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Projectile, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)
        self.speed = 20
        self.direction = direction
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update(self):
        #* Mueve el proyectil en la dirección dada
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        #* Elimina el proyectil si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > self.screen_width or self.rect.bottom < 0 or self.rect.top > self.screen_height:
            self.kill()