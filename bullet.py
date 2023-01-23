import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = ai_game.settings.bullet_img
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect.move_ip(5,0)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)