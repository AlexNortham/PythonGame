import pygame, sys
from pytmx.util_pygame import load_pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
tmx_data = load_pygame('gameMap.tmx')
spriteGroup = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    for layer in tmx_data.layers:
        if hasattr(layer, 'data'):
            for x, y, surf in layer.tiles():
                if x >= 490 & x <= 509 & y >= 480 & y <= 499:
                    pos = (x * 32, y * 32)
                    Tile(pos=pos, surf=surf, groups=spriteGroup)
    spriteGroup.draw(screen)
    pygame.display.update()
