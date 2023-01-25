import os
import uvicorn
from fastapi import FastAPI

from routes.snake_routes import getSnake

app = FastAPI()

app.include_router(getSnake(), prefix='/api/game')

def normalizePort(port):
    if (port is None):
        return 8080
    
    if (type(port) is str):
        return int(port)

    return port

if __name__ == "__main__":
    uvicorn.run("main:app", port=normalizePort(os.environ.get("PORT") or os.environ.get("API_PORT")))
