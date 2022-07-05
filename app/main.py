from fastapi import FastAPI

from app.routers.routers import user_router

app = FastAPI()

app.include_router(router=user_router, prefix="/user")
