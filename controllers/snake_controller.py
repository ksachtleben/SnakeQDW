from utils.game import Game

class SnakeController:
    def __init__(self):
        self.game = Game()

    def get_snake_game(self):
        return self.game.get_game_screen()