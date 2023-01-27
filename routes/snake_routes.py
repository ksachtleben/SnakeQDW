from fastapi import APIRouter
from controllers.snake_controller import SnakeController


def get_snake_game():

    router = APIRouter()

    snake_controller = SnakeController()

    @router.get("/")
    def get_snake_game():
        return snake_controller.get_snake_game()

    return router