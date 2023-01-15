from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer, String, Boolean,Text
from sqlalchemy.sql.expression import text

class Recommended(Base):
    __tablename__ = "recommended_q"
    id = Column(Integer,primary_key=True, nullable = False)
    question = Column(String(255), nullable = False)
    description = Column(Text, nullable = False)
    priority =  Column(String(255), nullable = False, server_default="LOW")