from .. import schemas
from .. import models
from .. import utils
from fastapi import  FastAPI,Response,status, HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from pydantic import BaseModel

router = APIRouter()

@router.post("/users", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)    
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hashedPassword = pwd_context.hash(user.password)
    # user.password = hashedPassword
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users/{id}',response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()
    return data