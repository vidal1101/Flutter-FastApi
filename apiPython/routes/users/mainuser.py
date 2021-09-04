from fastapi import APIRouter

routeruser = APIRouter(prefix="/user")

@routeruser.get("/fetchall")
async def fetchall_users():
    return {"fecth users"}


