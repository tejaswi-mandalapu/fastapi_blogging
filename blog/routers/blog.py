from fastapi import APIRouter, Depends,status,HTTPException
from ..import schemas, models,database
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router=APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db)
    
@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.create(request,db)
    
@router.get('/{id}',status_code=200 ,response_model=schemas.ShowBlog)
def show(id:int, db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.show(id,db)
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
   return blog.update(id, request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def remove(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.remove(id,db)




