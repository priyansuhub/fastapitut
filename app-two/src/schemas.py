from typing import Optional
from .database import Base
from sqlalchemy import TIMESTAMP, Column,Integer, String, Boolean
from sqlalchemy.sql.expression import text 
from pydantic import BaseModel, EmailStr

class RequestQuestion(BaseModel):
    question:str
    description:str
    priority:Optional[str]="LOW"