import pygame


class Tile(pygame.sprite.Sprite):
    SIZE = (WIDTH, HEIGHT) = (40, 40)  # 40x40

    dic_colors = {'yellow': (255, 239, 25), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0),
                  'blue': (0, 0, 255), 'orange': (239, 127, 26), 'black': (0, 0, 0)}

    def __init__(self, square_type, font, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.square_type = square_type
        self.text = self.set_text()
        self.color = self.set_color()
        self.font = font
        self.image = pygame.Surface(Tile.SIZE).convert()
        self.image.fill(self.color)
        label = self.font.render(str(self.text), 0, self.dic_colors['white'])
        coords = (Tile.WIDTH / 2. - (label.get_rect().width / 2.), Tile.HEIGHT / 2. - (label.get_rect().height / 2.))
        self.image.blit(label, coords)
        self.rect = self.image.get_rect(center=self.pos)

    #  self.value = 0
    #  self.quantity = 0

    def set_color(self):
        if self.square_type == "Normal":
            return self.dic_colors['white']
        elif self.square_type == "DL":
            return self.dic_colors['blue']
        elif self.square_type == "DP":
            return self.dic_colors['orange']
        elif self.square_type == "TL":
            return self.dic_colors['green']
        elif self.square_type == "TP":
            return self.dic_colors['red']
        elif self.square_type == "Start":
            return self.dic_colors['black']
        elif self.square_type == "Letter":
            return self.dic_colors['yellow']

    def set_text(self):
        if self.square_type == "Normal" or self.square_type == "Start" or self.square_type == "Letter":
            return ""
        else:
            return self.square_type
