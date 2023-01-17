from .database import engine, get_db
from . import models
from fastapi import  APIRouter, FastAPI,Response,status, HTTPException,Depends
from .view import questions
from .view import auth
from .view import user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(questions.router)
app.include_router(auth.router)
app.include_router(user.router)

