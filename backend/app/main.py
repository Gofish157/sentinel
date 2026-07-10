from fastapi import FastAPI
from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.logging import configure_logging
from app.modules.system.router import router as system_router

configure_logging()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan
)

app.include_router(system_router)
