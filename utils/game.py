import pygame
import random
from utils.food import Food
from utils.snake import Snake
from utils.obstacle import Obstacle
from utils.energy import QuantumEnergy
import math

class Game:
    def __init__(self):
        pygame.init()
        self.width = 900
        self.height = 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.obstacle1 = Obstacle(self.screen, self.width // 2, self.height // 301)
        self.obstacle2 = Obstacle(self.screen, self.width - 300, self.height // 301)
        self.running = True
        self.can_tunnel = False
        self.snake = Snake(self.screen, self.can_tunnel)
        self.food = Food(self.screen)
        self.time = 0
        self.time_increment = 0.1
        self.energy = QuantumEnergy(self.time)
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(-1, 0)
                elif event.key == pygame.K_UP:
                    self.snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, 1)

    def update(self):
        self.snake.move()
        self.time += self.time_increment
        self.obstacle2.width = 600
        self.obstacle2.x =  750 + math.cos(self.time) * 150
        if self.snake.check_collision(self.food):
            self.snake.grow()
            self.food.spawn()
        if not self.snake.check_collision_screen(self.width, self.height):
            self.running = False
            print("Game Over")
            pygame.quit()
        if self.snake.check_collision_obstacle(self.obstacle1) or self.snake.check_collision_obstacle(self.obstacle2):
            self.running = False
            print("Game Over")
            pygame.quit()
        if self.food.is_in_obstacle(self.obstacle1) or (self.snake.can_tunnel and self.food.x < self.obstacle1.x) or (self.food.is_in_obstacle(self.obstacle2)) or (not self.snake.can_tunnel and self.food.x > self.obstacle1.x):
            self.food.spawn()
        

    def draw(self):
        self.screen.fill((0, 0, 51))
        self.snake.draw()
        self.food.draw()
        self.obstacle1.draw()
        self.obstacle2.draw()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.energy.calc_energy()
            pygame.time.wait(50)
        return 1,2,3

