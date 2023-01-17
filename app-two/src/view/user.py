from .. import schemas
from .. import models
from .. import utils
from sqlalchemy.orm import Session
from fastapi import  FastAPI,Response,status, HTTPException,Depends,APIRouter
from ..database import engine, get_db

router = APIRouter()

@router.post("/user")
def user_post(user:schemas.RequestUser, db:Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}", response_model=schemas.ResponseUser)
def user_get(id: int, db:Session = Depends(get_db)):
    data = db.query(models.Users).filter(models.Users.id == id).first()
    return data



