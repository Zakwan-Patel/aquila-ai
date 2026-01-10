from fastapi import FastAPI
from app.api.rag_api import router as rag_router
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="Enterprise AI Knowledge & Decision Assistant",
    version="0.1.0"
)

app.include_router(rag_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment
    }
from fastapi import FastAPI
from app.api.rag_api import router as rag_router
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="Enterprise AI Knowledge & Decision Assistant",
    version="0.1.0"
)

app.include_router(rag_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment
    }
