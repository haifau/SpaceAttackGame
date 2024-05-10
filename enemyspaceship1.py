import pygame

class EnemySpaceShip1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemy_spaceship_1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.delta = 5
        self.current_direction = "up"

    def move_enemy_ship(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())