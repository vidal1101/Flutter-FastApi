#imports for the workspace 
from fastapi import FastAPI

from routes.users import mainuser as mainuser

app = FastAPI(title="FastAPI-Usuarios",
             description="simple rest-full api with mysql",
             version="1.0")

app.include_router(mainuser.routeruser) 




