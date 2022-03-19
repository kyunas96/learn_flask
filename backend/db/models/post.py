from .base import Base
from sqlalchemy import (Column, Integer, String,
                        DateTime, UniqueConstraint, ForeignKey)
from sqlalchemy.orm import relationship
import datetime


class Post(Base):
    __tablename__ = 'post'
    id = Column('id', Integer, primary_key=True)
    user = Column('user', ForeignKey('user.id'), nullable=False)
    name = Column('name', String(64), nullable=False)
    image_url = Column('image_url', String(1024), nullable=False)
    description = Column('description', String(1024), nullable=True)
    created_at = Column('created_at', DateTime, nullable=False)
    likes = relationship('Like', cascade='all, delete-orphan')
    __tableargs__ = (
        UniqueConstraint('name', 'user_id')
    )

    def __init__(self, user_id, name, image_url, description):
        self.user_id = user_id
        self.name = name
        self.image_url = image_url
        self.description = description
        self.created_at = datetime.datetime.utcnow()
