from fastapi import FastAPI

from app.config import setting
from app.core.databases.db import Base,engine
from app import apis


app = FastAPI(title=setting.API_NAME, version= setting.API_VERSION)
app.include_router(apis.router)
Base.metadata.create_all(engine)

