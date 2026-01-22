from fastapi import FastAPI
from routers import metrics,aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API utilities",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    """
    This is the Hello API, just for testing
    """
    return {"message": "Hello Dosto, This is DevOps Utilities API"}

app.include_router(aws.router,prefix="/aws")
app.include_router(metrics.router)
