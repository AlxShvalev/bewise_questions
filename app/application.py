from fastapi import FastAPI

from app.api.routers.questions_router import router as questions_router
from app.core.config import settings


def create_app() -> FastAPI:
    """Create FastAPI application"""
    app = FastAPI(
        title=settings.title,
        debug=settings.debug,
        root_path=settings.root_path
    )

    app.include_router(questions_router)

    return app
