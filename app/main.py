from fastapi import FastAPI

app = FastAPI(
    title="Fintech Core Engine",
    version="0.1.0",
    description="High-Throughput Payment Webhook & Transaction Processing Engine",
)

@app.get("/healthz", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "service": "fintech-core-engine",
        "version": "0.1.0",
    }