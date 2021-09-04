#imports for the workspace 
from fastapi import FastAPI
from starlette.responses import RedirectResponse

#routes
from routes.users import mainuser as mainuser

app = FastAPI(title="FastAPI-Usuarios",
             description="simple rest-full api with mysql",
             version="1.0")

#includes
app.include_router(mainuser.routeruser) 

#route index
@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")





