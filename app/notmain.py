from typing import Optional
from fastapi import  FastAPI,Response,status, HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
import mysql.connector
from . import schemas
from . import models
from . import utils
from .database import engine, get_db
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

