from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting: {settings.app_name}")

    try:
        yield

    finally:
        logger.info(f"Stopping: {settings.app_name}")
