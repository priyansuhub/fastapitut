from .database import engine, get_db
from . import models
from fastapi import  APIRouter, FastAPI,Response,status, HTTPException,Depends
from .view import questions


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(questions.router)