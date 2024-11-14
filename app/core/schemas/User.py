from pydantic import Field, BaseModel

class User(BaseModel):
    name: str = Field(min_length=1)
    mobile: str = Field(min_length=10)

