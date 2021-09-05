from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import schema
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from providers.database import Sesionlocal
from typing import List
import providers.schemas
import models.usermodel

#objeto tipó APIRouter
routeruser = APIRouter(prefix="/user")

#retorna la conexion con una sesion
def get_db():
    try:
        db = Sesionlocal()
        yield db
    finally:
        db.close()


#routes
@routeruser.get("/fetchall-usuarios", response_model=List[providers.schemas.User] )
async def fetchall_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.usermodel.User).all()
    print(usuarios)
    return usuarios


@routeruser.post("/create-usuario", response_model=providers.schemas.User)
async def create_user(entrada:providers.schemas.User,db:Session=Depends(get_db)):
    usuario = models.usermodel.User(username= entrada.username, 
                                    nombre = entrada.nombre,
                                    contrasena = entrada.contrasena,
                                    estado= entrada.estado,
                                    avatar= entrada.avatar)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


@routeruser.put("/update-user", response_model=providers.schemas.User)
async def update_user(usuario_id:int, entrada:providers.schemas.UserUpdate,
                                                db:Session=Depends(get_db)):

    usuario = db.query(models.usermodel.User).filter_by(id=usuario_id).first()
    usuario.nombre= entrada.avatar
    db.commit()
    db.refresh(usuario)
    return usuario


@routeruser.delete("/delete-user", response_model=providers.schemas.Respuesta)
async def delete_user(usuario_id:int,db:Session=Depends(get_db) ):
    usuario = db.query(models.usermodel.User).filter_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    response = providers.schemas.Respuesta(messaje="delete success")
    return response




