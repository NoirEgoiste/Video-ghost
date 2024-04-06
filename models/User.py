from . import Base, Video


class User(Base):
    __tablename__ = 'User'

    username: str
    password: str
    videos: list[Video]