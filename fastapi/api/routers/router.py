from fastapi import APIRouter

from api.routers import greetings

api_router = APIRouter()
api_router.include_router(greetings.router, tags=["greetings"], prefix="/greetings")
