from fastapi import FastAPI
from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan
)
