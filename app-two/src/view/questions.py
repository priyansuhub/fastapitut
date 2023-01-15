from fastapi import  APIRouter, FastAPI,Response,status, HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import engine, get_db
from pydantic import BaseModel
from typing import List
from .. import schemas
from .. import models
router = APIRouter(tags=['Questions'])

@router.get("/")
def get_questions():
    return "Data:Loda"

@router.post("/questions")
def post_questions(ques: schemas.RequestQuestion, db: Session = Depends(get_db)):
    new_ques = models.Recommended(**ques.dict())
    db.add(new_ques)
    db.commit()
    db.refresh(new_ques)
    return {"new_question": new_ques}