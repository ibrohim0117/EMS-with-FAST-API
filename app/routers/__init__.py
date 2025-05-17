from fastapi import APIRouter
from . import index, auth, user

routers = APIRouter()

routers.include_router(index.router)
routers.include_router(auth.router)
routers.include_router(user.router)
