# esquemas segun el caso que desee hacer en la base de datos a traves de la API 
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    username:str
    nombre: str
    contrasena: str
    estado: int
    avatar: Optional[str]

    class Config: 
        orm_mode=True


class UserUpdate(BaseModel):
    avatar:str

class UserGet(BaseModel):
    username:str

class Respuesta(BaseModel):
    mensaje:str