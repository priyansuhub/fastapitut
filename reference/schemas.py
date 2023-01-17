from typing import Optional
from .database import Base
from sqlalchemy import TIMESTAMP, Column,Integer, String, Boolean
from sqlalchemy.sql.expression import text 
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    role: Optional[str] = "USER"

class TestUser:
    title: str
    content: str
    published: bool = False
    owner_id: int