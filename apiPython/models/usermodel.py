from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import base
from providers.database import Base

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    username = Column(String(50))
    nombre = Column(String(50))
    contrasena = Column(String(200), nullable= False, unique=True)
    estado = Column(Integer)
    avatar = Column(String(400) , nullable=True)