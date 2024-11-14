from app.core.models.models import User as user_model
from app.core.schemas import User as user_schema
from sqlalchemy.orm import Session


async def create_user(user: user_schema,db: Session):
    userr = user_model(name = user.name, mobile = user.mobile)
    db.add(userr)
    db.commit()
    db.refresh(userr)
    return userr
    