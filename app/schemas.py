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

