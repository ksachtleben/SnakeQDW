import pygame

class Obstacle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (255, 153, 51)
        self.height = x
        self.width = 45

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))