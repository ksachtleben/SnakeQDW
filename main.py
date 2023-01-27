import os
import uvicorn
from fastapi import FastAPI

from routes.snake_routes import get_snake_game

app = FastAPI()

app.include_router(get_snake_game(), prefix='/api/game')

def normalizePort(port):
    if (port is None):
        return 8080
    
    if (type(port) is str):
        return int(port)

    return port

if __name__ == "__main__":
    uvicorn.run("main:app", port=normalizePort(os.environ.get("PORT") or os.environ.get("API_PORT")))

#http://127.0.0.1:8000/api/game/