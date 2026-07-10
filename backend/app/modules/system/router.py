from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "OK"
    }

@router.get("/")
def root():
    return {
        "name": settings.app_name
    }