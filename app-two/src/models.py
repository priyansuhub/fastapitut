from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer, String, Boolean,Text
from sqlalchemy.sql.expression import text

class Recommended(Base):
    __tablename__ = "recommended_q"
    id = Column(Integer,primary_key=True, nullable = False)
    question = Column(String(255), nullable = False)
    description = Column(Text, nullable = False)
    priority =  Column(String(255), nullable = False, server_default="LOW")

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, nullable = False)
    email = Column(String(64), nullable=False,unique=True)
    password = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False,server_default="USER")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
