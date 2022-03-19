from .base import Base
from .like import Like
from .follow import Follow
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import bcrypt
import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(32), nullable=False, unique=True)
    email = Column('email', String(64), nullable=False, unique=True)
    password = Column('password', String(), nullable=False)
    location = Column('location', String(128), nullable=True)
    bio = Column('bio', String(256), nullable=True)
    created_at = Column('date_created', DateTime, nullable=False)
    posts = relationship('Post', backref='user', cascade='all, delete-orphan')
    following = relationship('User', secondary=Follow,
                             primaryjoin=lambda: User.id == Follow.c.follower_id,
                             secondaryjoin=lambda: User.id == Follow.c.followee_id,
                             backref='followers'
                             )
    likes = relationship('Likes', Like, backref='user',
                         cascade='all, delete-orphan')

    @staticmethod
    def create_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password, salt)

    def verify_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.checkpw(password, salt)

    def __init__(self, username, email, password):
        if not username or not email:
            raise Exception('Missing fields for User instance')
        self.username = username
        self.email = email
        self.password = User.create_password(password)
        self.date_created = datetime.datetime.utcnow()
