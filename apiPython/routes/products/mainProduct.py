from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import schema
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from providers.database import Sesionlocal
from typing import List
import providers.shemaProduct
import models.usermodel

routerproduct = APIRouter(prefix="/product")

#retorna la conexion con una sesion
def get_db():
    try:
        db = Sesionlocal()
        yield db
    finally:
        db.close()

@routerproduct.get("/prueba")
async def pruebaProduct(db:Session=Depends(get_db)):
    return "success, in process"