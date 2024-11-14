from fastapi import APIRouter
from app.v1.routes import user_routes

router = APIRouter()
router.include_router(user_routes.router,prefix='/users',tags=['BOOKS'])