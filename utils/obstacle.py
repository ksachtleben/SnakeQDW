import pygame

class Obstacle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = 0
        print(self.x, self.y)
        self.color = (255, 153, 51)
        self.height = y
        self.width = 50

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))