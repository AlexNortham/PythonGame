import sys, pygame


class SpriteSheet:

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"inable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, colourkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colourkey is not None:
            if colourkey is -1:
                colourkey = image.get_at((0, 0))
            image.set_colorkey(colourkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colourkey=None):
        return [self.image_at(rect, colourkey) for rect in rects]

    def load_strip(self, rect, image_count, colourkey=None):
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colourkey)
