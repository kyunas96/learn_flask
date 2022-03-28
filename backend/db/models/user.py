from venv import create

from flask import session
from .base import Base
from .like import Like
from .follow import Follow
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import relationship
from .utils.user import create_session_token
import bcrypt
import datetime


class User(Base):
    __tablename__ = 'users'
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
        password_as_bytes = bytes(password.encode())
        hashed_pw_as_bytes = bcrypt.hashpw(password_as_bytes, salt)
        return hashed_pw_as_bytes.decode('utf-8')

    @staticmethod
    def reset_session_token(user_id):
        new_session_token = create_session_token()
        session = Base.create_session()
        session.query(User).filer(User.id == user_id).update({
            User.session_token: new_session_token
        })
        session.commit()
        session.close()

    @staticmethod
    def update_user(user_id, data):
        session = Base.create_session()
        session.query(User).filter(User.id == user_id).update(data)
        session.commit()
        session.close()

    @staticmethod
    def get_user_from_id(user_id):
        session = Base.create_session()
        try:
            user = session.query(User).filter(User.id == user_id).one()
            print(user)
            return user
        except NoResultFound as e:
            return None

    @staticmethod
    def get_user(username):
        session = Base.create_session()
        try:
            user = session.query(User).filter(User.username == username).one()
            return user
        except NoResultFound as e:
            return None

    @staticmethod
    def get_from_session_token(session_token):
        session = Base.create_session()
        try:
            user = session.query(User).filter(User.session_token == session_token).one()
            print(f"user: {user}")
            return user
        except NoResultFound as e:
            return None

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = User.create_password(password)
        self.date_created = datetime.datetime.utcnow()
        self.session_token = create_session_token()


    def verify_password(self, password):
        password_as_bytes = bytes(password.encode())
        hashed_as_bytes = bytes(self.password.encode())
        if bcrypt.checkpw(password_as_bytes, hashed_as_bytes):
            print("CORRECT")
            return True
        else:
            print("INCORRECT")
            return False
