from fastapi import FastAPI
from app import models, schemas, crud, database
from app.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health():
    return {"status": "OK"}
