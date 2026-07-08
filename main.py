from fastapi import FastAPI
from app.routers import users
from logger import logger
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)
app.include_router(users.router)

@app.get("/")
def root():
    logger.info("Home endpoint called")
    return {"message": "API Running"}
