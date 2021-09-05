# esta seria la clase conexion con sqlalchemy a mysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "mysql+mysqlconnector://root:Runo1101@localhost:3306/company"

engine = create_engine(database_url)

Sesionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()