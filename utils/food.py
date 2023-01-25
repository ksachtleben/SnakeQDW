import pygame
import random

class Food:
    def __init__(self, screen):
        self.screen = screen
        self.size = 5
        self.x = random.randint(0, self.screen.get_width() - self.size)
        self.y = random.randint(0, self.screen.get_height() - self.size)
        self.x = 0
        self.y = 0
        self.color = (255, 0, 0)
        self.spawn()
        
    def is_in_obstacle(self, obstacle):
        if self.x >= obstacle.x and self.x < obstacle.x + obstacle.width and self.y >= obstacle.y and self.y < obstacle.y + obstacle.height:
            return True
        return False

    def spawn(self):
        self.x = random.randint(0, self.screen.get_width() - self.size)
        self.y = random.randint(0, self.screen.get_height() - self.size)
        self.x = self.x - (self.x % 5)
        self.y = self.y - (self.y % 5)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))