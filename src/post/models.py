from sqlalchemy import Column, Integer, String

from src.database import Base


class Post(Base):
    __tablename__ = 'post'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String)
    description: str = Column(String)
