# crear la estructura de la tablas a crear en la base de datos
from sqlalchemy import Column, Integer, String
from providers.database import Base

class User(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    username = Column(String(50))
    nombre = Column(String(50))
    contrasena = Column(String(200), nullable= False, unique=True)
    estado = Column(Integer)
    avatar = Column(String(400) , nullable=True)


class Product(Base):
    __tablename__='Product'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nameProduct = Column(String(50))
    description = Column(String(200))
    price = Column(Integer)
    imageProduct = Column(String(600), nullable=True)
    stock = Column(Integer)