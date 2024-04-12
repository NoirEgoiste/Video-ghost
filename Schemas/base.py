from pydantic import BaseModel


class Base(BaseModel):
    orm_mode = True
