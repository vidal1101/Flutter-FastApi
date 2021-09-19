# Flutter-FastApi
Creación de una API con el framework FastApi. 
https://fastapi.tiangolo.com/

utilizando sqlalchemy de ORM para comunicarme con mysql. 
documentacion de implementacion:
https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/#sqlalchemy-engine

-------------------------------------------------------------------------------------

API. 

estructura de carpeta y rutas

├── main.py

│ └── routers

│ │└── users

│ │ ├── init.py

│ │ ├── mainuser.py

│ │└── products

│ │ ├── init.py

│ │ ├── mainProduct.py

│ └── providers

│ │ ├── init.py

│ │ ├── database.py

│ │ ├── schemas.py

│ │ ├── schemaProduct.py

│ └── models

│ │ ├── usermodel.py

-------------------------------------------------------

implementaciones:

instalar las dependencias con el gestor de paquetes de pyrthon: pip install -r requirements.txt

cambiar la URL de conexion segun el motor de base de datos, 
apyPython/providers/database.py

en este caso es una conexion con mysql. 

    database_url = "mysql+mysqlconnector://user:password@localhost:3306/nameDatabase"

probar la api apy.

    uvicorn main:app --reload  

-------------------------------------------------------------------------------------

FLUTTER. 

EN PROCESO... 