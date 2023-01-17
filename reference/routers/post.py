from typing import List
from .. import schemas
from .. import models
from .. import utils,Oauth2
from fastapi import  APIRouter, FastAPI,Response,status, HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import engine, get_db
from pydantic import BaseModel

router = APIRouter(tags=['Post'])

class Post(BaseModel):
    title: str
    content: str
    published: bool = False


@router.get("/", response_model=List[schemas.TestUser])
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"status": posts}

@router.post("/posts")
def post_data(post:Post ,db: Session = Depends(get_db),user_id:int = Depends(Oauth2.get_current_user)):
    print(user_id)
    newPost = models.Post(**post.dict())
    db.add(newPost)
    db.commit()
    db.refresh(newPost)
    return {"data": newPost}

@router.get("/posts/{id}")
def get_post_by_id(id:int,db: Session = Depends(get_db), current_user: int = Depends(Oauth2.get_current_user)):
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    print(current_user)
    return posts

@router.delete("/posts/{id}")
def delete_post_by_id(id: int,db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id)
    posts.delete(synchronize_session=False)
    db.commit()

@router.put("/posts/{id}")
def update_post_by_id(id: int,test: Post,db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    post_query.update(test.dict(), synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}