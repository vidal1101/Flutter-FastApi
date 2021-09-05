#imports for the workspace 
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy import engine
from starlette.responses import RedirectResponse
import models.usermodel 
from providers.database import Sesionlocal, engine
from sqlalchemy.orm import session

#objetos de apirouter a incluir
from routes.users import mainuser as mainuser

#crear las tablas de las estructura de la clase. 
models.usermodel.Base.metadata.create_all(bind=engine)

#objeto fastapi
app = FastAPI(title="FastAPI-Usuarios",
             description="simple rest-full api with mysql",
             version="1.0")


#includes
app.include_router(mainuser.routeruser) 


#route index
@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")





