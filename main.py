import pygame, sys
from pytmx.util_pygame import load_pygame
from SpriteSheet import SpriteSheet
from random import randint

playerIcons = SpriteSheet("playersprite.png")
walkingRect = (9, 15, 14, 27)
walkingImage = playerIcons.image_at(walkingRect)


# must in future make a function that returns array of images


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = walkingImage
        self.rect = self.image.get_rect(cente=pos)
        self.direction = pygame.math.Vector2
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2(490*32, 487*32)

        self.ground_rect = (0, 0, 1000 * 32, 1000 * 32)

    def custom_draw(self):
        self.display_surface.blit(self.offset)


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

tmx_data = load_pygame('gameMap.tmx')
spriteGroup = pygame.sprite.Group()

for layer in tmx_data.layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            if x >= 490 & x <= 509 & y >= 480 & y <= 499:
                pos = (x * 32, y * 32)
                Tile(pos=pos, surf=surf, groups=spriteGroup)

camera_group = pygame.sprite.Group()
Player((490*32, 487*32), camera_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')

    spriteGroup.draw(screen)
    pygame.display.update()
