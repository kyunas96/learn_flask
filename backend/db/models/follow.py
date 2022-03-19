from .base import Base
from sqlalchemy import (
    Column, Integer, UniqueConstraint, DateTime, ForeignKey)
import datetime


class Follow(Base):
    __tablename__ = 'follow'
    follower_id = Column('follower_id', Integer,
                         ForeignKey('user.id'), primary_key=True)
    followee_id = Column('followee_id', Integer,
                         ForeignKey('user.id'), primary_key=True)
    created_at = Column('created_at', DateTime, nullable=False)
    __tableargs__ = (
        UniqueConstraint('follower_id', 'followee_id')
    )

    def __init__(self, follower_id, followee_id):
        self.follower_id = follower_id
        self.followee_id = followee_id
        self.created_at = datetime.datetime.utcnow()
