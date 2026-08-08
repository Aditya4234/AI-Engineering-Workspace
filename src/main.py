from fastapi import FastAPI

app = FastAPI(
    title="AI engineering workspace",
    description="AI Engineering Bootcamp Backend",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "AI Engineering Bootcamp Ready"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
