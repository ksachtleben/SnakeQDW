from fastapi import APIRouter
from controllers.snake_controller import GameController

def getSnake():
    router = APIRouter()

    print('route')

    controller = GameController()

    return controller.game()