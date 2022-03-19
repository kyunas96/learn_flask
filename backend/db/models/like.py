from .base import Base
import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Like(Base):
    __tablename__ = 'like'
    post = Column('post_id', Integer, ForeignKey('post.id'), primary_key=True)
    user = Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
    created_at = Column('created_at', DateTime, nullable=False)

    def __init__(self, post_id, user_id):
        self.post = post_id
        self.user = user_id
        self.created_at = datetime.datetime.utcnow()
        
