from fastapi import FastAPI
from .import models
from .database import engine
from .routers import blog,user,authentication



app=FastAPI()
   

models.Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

 
#def get_db():
#    db = SessionLocal()
#    try:
#     finally:
#       db.close()




#@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
#def all(db:Session=Depends(get_db)):
#    blogs=db.query(models.Blog).all()
#   return blogs




