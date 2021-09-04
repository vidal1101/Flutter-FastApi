#imports for the workspace 
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy import engine
from starlette.responses import RedirectResponse
import providers.shemas
import models.usermodel 
from providers.database import Sesionlocal, engine
from sqlalchemy.orm import session

#routes
from routes.users import mainuser as mainuser

models.usermodel.Base.metadata.create_all(bind=engine)


app = FastAPI(title="FastAPI-Usuarios",
             description="simple rest-full api with mysql",
             version="1.0")

def get_db():
    try:
        db = Sesionlocal()
        yield db
    finally:
        db.close()

#includes
app.include_router(mainuser.routeruser) 

#route index
@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")





