import pygame

class Player(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healf = 100
        self.attack = 10
        self.velocity = 10
        self.image = pygame.image.load('/Users/benjamin/Documents/GitHub/transverse/image/pngtree-sprite-sheet-of-the-flash-character-with-animation-for-creating-2d-png-image_5268150-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity





class technoblade:
    def __init__(self):
        self.player = Player()
        self.pressed = {}