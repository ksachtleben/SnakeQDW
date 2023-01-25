from utils.game import Game

class GameController:
    def __init__(self):
        self._game: Game = Game()

    def game(self):
        
        self._game.run()
        
        return {}
        '''if collision:
            return "Game Over. Final Score: {}".format(score)
        else:
            return {"snake_pos": snake_pos, "score": score}'''