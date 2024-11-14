from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.schemas.User import User as user_schema
from app.core.models.models import User as user_model
from app.core.databases.db_util import get_db
from app.v1.services import user_service


router  = APIRouter()

@router.post('/')
async def create_user(users: user_schema, db: Session = Depends(get_db)):
    user_s = await user_service.create_user(user=users, db=db)

    return user_s