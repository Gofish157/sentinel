from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.database import engine
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting: {settings.app_name}")

    logger.info(f"Connecting to PostgreSQL")
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    logger.info(f"Database connected successfully")
    try:
        yield

    finally:
        logger.info(f"Stopping: {settings.app_name}")
