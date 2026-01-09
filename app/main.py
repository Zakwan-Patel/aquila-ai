from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="Enterprise AI Knowledge & Decision Assistant",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
        "message": "Aquila AI backend is running"
    }
