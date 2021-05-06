import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from constants import ROOT_PATH
from container import Container
from presentation import controller


def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml(f"{ROOT_PATH}/config.yaml")
    container.wire(modules=[controller])

    app = FastAPI()
    app.include_router(controller.router)
    app.container = container
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080", "http://localhost:8080/*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
