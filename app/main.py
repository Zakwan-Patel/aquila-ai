from fastapi import FastAPI

app = FastAPI(
    title="Aquila AI",
    description="Enterprise AI Knowledge & Decision Assistant",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Aquila AI backend is running"
    }
