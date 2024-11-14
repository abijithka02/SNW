from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


user_db = "sqlite:///database.db"
engine = create_engine(user_db)


Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

