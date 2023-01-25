import pygame
import random

class Snake:
    def __init__(self, screen, can_tunnel):
        self.screen = screen
        self.can_tunnel = can_tunnel
        self.x = 0
        self.y = 0
        self.color = (51, 255, 153)
        self.size = 5
        self.speed = 5
        self.direction = "right"
        self.body = [(self.x, self.y)]


    def move(self):
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed

        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def check_collision(self, food):
        snake_head = self.body[0]
        if snake_head[0] == food.x and snake_head[1] == food.y:
            return True
        return False

    def check_collision_obstacle(self, obstacle):
        if self.can_tunnel:
            return False
        for segment in self.body:
            if segment[0] >= obstacle.x and segment[0] < obstacle.x + obstacle.width and segment[1] >= obstacle.y and segment[1] < obstacle.y + obstacle.height:
                return True
        return False

    def check_collision_screen(self,x,y):
        snake_head = self.body[0]
        if snake_head[0] < 0 or snake_head[0] > x - self.size or snake_head[1] < 0 or snake_head[1] > y - self.size:
            return False
        return True

    def change_direction(self, dx, dy):
        if dx == -1 and self.direction != "right":
            self.direction = "left"
        elif dx == 1 and self.direction != "left":
            self.direction = "right"
        elif dy == -1 and self.direction != "down":
            self.direction = "up"
        elif dy == 1 and self.direction != "up":
            self.direction = "down"
    
    def grow(self):
        last_segment = self.body[-1]
        self.body.append(last_segment)    

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.screen, self.color, (segment[0], segment[1], self.size, self.size))