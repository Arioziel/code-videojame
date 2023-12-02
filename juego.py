import pygame
from pygame import sprite, transform, key, image

class Personaje(sprite.Sprite):
    def __init__(self, image_path, x, y):  # Cambiado el nombre de la variable
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image_path), (25, 30))  # Utilizamos el nuevo nombre
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= 5
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < screen.get_width() - self.rect.width:
            self.rect.x += 5
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0:
            self.rect.y -= 5
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.y < screen.get_height() - self.rect.height:
            self.rect.y += 5

class pared:
    def __init__(self, ancho, longitud, x, y, color=(15, 42, 8)):
        self.ancho = ancho 
        self.longitud = longitud
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, longitud, ancho)

    def dibujar(self, tamaño):
        pygame.draw.rect(tamaño, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

Personaje_image_path = "pagman2.jpg"
pagman2 = Personaje(Personaje_image_path, 100, 100)
pared1 = pared(15, 250, 9, 100)
pared2 = pared(15,250, 9, 200)


all_sprites = pygame.sprite.Group()
all_sprites.add(pagman2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
         

    all_sprites.update()

    screen.fill((255, 255, 255))
    pared1.dibujar(screen)
    pared2.dibujar(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(100)



    


pygame.quit()