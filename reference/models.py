from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer, String, Boolean
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable = False)
    title = Column(String(16), nullable=False)
    content = Column(String(16), nullable=False)
    published = Column(Boolean, server_default='1', nullable=False) 
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable = False)
    email = Column(String(64), nullable=False,unique=True)
    password = Column(String(64), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))

