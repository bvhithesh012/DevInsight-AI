from fastapi import FastAPI

app = FastAPI(
    title="DevInsight AI",
    description="AI-powered Developer Hiring & Evaluation Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DevInsight AI 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "service": "DevInsight AI Backend"
    }