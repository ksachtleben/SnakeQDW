import pygame
import random
from utils.food import Food
from utils.snake import Snake
from utils.obstacle import Obstacle
from utils.energy import QuantumEnergy
import math

class Game:
    def __init__(self):
        self.width = 800
        self.height = 300
        self.time = 0
        self.time_increment = 0.1
        self.running = True
        self.can_tunnel = False
        self.screen = None

    
    def get_game_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.obstacle1 = Obstacle(self.screen, 0.25*self.width, self.height)
        self.obstacle2 = Obstacle(self.screen, 5*self.width/8, self.height)
        self.snake = Snake(self.screen, self.can_tunnel)
        self.food = Food(self.screen)
        self.run()
        pygame.display.update()
        return self.screen
        
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
        self.energy = QuantumEnergy(self.time)
        self.obstacle2.width = 500
        self.obstacle2.x =  700 + math.cos(self.time/10) * 250
        if self.snake.check_collision(self.food):
            self.snake.grow()
            self.snake.gainenergy()
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
            self.check_energy()
            self.draw()
            pygame.time.wait(50)
        return self.screen

    def check_energy(self):
        d = self.energy.calc_energy()
        values = list(d.values())
        for i, j in zip(values, values[1:]):
            if abs(j - i)/10 < 1 and i <= self.snake.energy <= j:
                self.can_tunnel = True
                self.snake.color = (204, 255, 51)
                break
        else:
            self.can_tunnel = False
            self.snake.color = (153, 153, 153)
