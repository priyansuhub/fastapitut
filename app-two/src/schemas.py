from typing import Optional
from .database import Base
from sqlalchemy import TIMESTAMP, Column,Integer, String, Boolean
from sqlalchemy.sql.expression import text 
from pydantic import BaseModel, EmailStr

class RequestQuestion(BaseModel):
    question:str
    description:str
    priority:Optional[str]="LOW"

class RequestUser(BaseModel):
    email:EmailStr
    password:str

class ResponseUser(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None
    role: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str