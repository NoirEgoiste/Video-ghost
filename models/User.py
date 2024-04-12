from sqlalchemy.orm import mapped_column

from . import Base, Videos


class User(Base):
    __tablename__ = "users"

    username: str
    email: mapped_column()
    password: str
    videos: list["Videos"]
