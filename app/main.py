from fastapi import FastAPI
from app.routers.historia import router as historia

app = FastAPI()

app.include_router(historia)