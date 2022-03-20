from venv import create
from .base import Base
from .like import Like
from .follow import Follow
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .utils.user import create_session_token
import bcrypt
import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username',
                      String(32),
                      nullable=False,
                      unique=True,
                      index=True)

    avatar_s3_object_id = Column(
        'avatar_s3_object_id', String(), nullable=True)
    email = Column('email', String(64), nullable=False, unique=True)
    password = Column('password', String(), nullable=False)
    session_token = Column('session_token',
                           String(),
                           index=True,
                           unique=True,
                           nullable=False)
    location = Column('location', String(128), nullable=True)
    bio = Column('bio', String(256), nullable=True)
    date_created = Column('date_created', DateTime, nullable=False)
    posts = relationship('Post', cascade='all, delete-orphan')
    following = relationship('User', secondary=Follow.__table__,
                             primaryjoin=lambda: User.id == Follow.follower_id,
                             secondaryjoin=lambda: User.id == Follow.followee_id,
                             backref='followers')
    likes = relationship('Like',
                         primaryjoin=lambda: User.id == Like.user,
                         cascade='all, delete-orphan')

    @staticmethod
    def create_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(b'password', salt)

    def verify_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.checkpw(b'password', salt)

    def __init__(self, username, email, password):
        if not username or not email:
            raise Exception('Missing fields for User instance')
        self.username = username
        self.email = email
        self.password = User.create_password(password)
        self.date_created = datetime.datetime.utcnow()
        self.session_token = create_session_token()

    def update_user(data):
        user_id = data.user.id
        user_data = {k: v for k, v in data.items() if v != 'id'}
        session = Base._Session_()
        session.query(User).filter(User.id == user_id).update(user_data)
        session.commit()
        session.close()
