from fastapi import APIRouter

routeruser = APIRouter(prefix="/user")

@routeruser.get("/")
@routeruser.get("/index")
async def index(): 
    return {"Welcome ":"FastApi-Usuarios"}

