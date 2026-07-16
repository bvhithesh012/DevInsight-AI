from app.api.auth import router as auth_router
from fastapi import FastAPI
from sqlalchemy import text
from app.api.resume import router as resume_router

from app.core.config import settings
from app.database.connection import engine

app = FastAPI(
    title="DevInsight AI",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(resume_router)

@app.get("/")
def root():
    return {
        "message": "DevInsight AI Backend Running"
    }


@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "Connected Successfully ✅"
        }

    except Exception as e:
        return {
            "database": "Connection Failed ❌",
            "error": str(e)
        }