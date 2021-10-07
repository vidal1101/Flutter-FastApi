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

App con un login y mostrando informacion de la API
haciendo uso de las dependencias en el arhivo pubspec.yaml

  http: ^0.12.1

    
estructura de carpetas de la aplicacion demo, se contendra dentro de userapp
en la carperta de Lib

├── lib

│ │└── main.dart

│ └── src

│ │└── pages

│ │ ├── myApp.dart

│ │ ├── Login.dart

│ │ ├── homepage.dart

│ │└── widget

│ │ ├── color,dart

│ │└── providers

│ │ ├── providers_user.dart

│ │└── models

│ │ ├── model_user.dart

en caso de posibles errores con los permisos de con null-satefy 


<img src="errorflutter.png">errorflutter.pngerrorflutter.png

-----------------------------

# Desarrollador
# Rodrigo Vidal
