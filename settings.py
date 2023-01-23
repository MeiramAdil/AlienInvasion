import pygame

class Settings:
    """Класс для хранения всех настроек игры."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load('images/space.bmp')
        self.bg = pygame.transform.scale(self.bg,(self.screen_width, self.screen_height))
        
        self.ship_speed = 4
        self.ship_limit = 3
        self.ship_img = pygame.image.load('images/our_starship.png')
        self.ship_img = pygame.transform.scale(self.ship_img,(134,158))

        self.bullet_speed = 3
        self.bullet_img = pygame.image.load('images/puh.png')
        self.bullet_img = pygame.transform.scale(self.bullet_img,(10,35))
        self.bullets_allowed = 3

        self.alien_img = pygame.image.load('images/alien_starship.png')
        self.alien_img = pygame.transform.scale(self.alien_img,(134,158))
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

        # Темп 
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
