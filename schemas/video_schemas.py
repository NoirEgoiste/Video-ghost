from pydantic import BaseModel


class Video(BaseModel):
    name: str
    url: str
