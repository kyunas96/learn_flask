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

    @classmethod
    def get_from_id(cls, id):
        return super(cls, cls).get_from_id(id)
        
    @staticmethod
    def create_password(password):
        salt = bcrypt.gensalt()
        password_as_bytes = bytes(password.encode())
        hashed_pw_as_bytes = bcrypt.hashpw(password_as_bytes, salt)
        return hashed_pw_as_bytes.decode('utf-8')

    def reset_session_token(self):
        new_session_token = create_session_token()
        ret = self.update({"session_token" : new_session_token})

    @staticmethod
    def get_from_session_token(session_token):
        session = Base.create_session()
        try:
            user = session.query(User).filter(User.session_token == session_token).one()
            print(f"user: {user}")
            return user
        except NoResultFound as e:
            return None

    def __init__(self, user_dict):
        self.username = user_dict['username']
        self.email = user_dict['email']
        self.password = User.create_password(user_dict['password'])
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

    def to_json(self):
        # print(f"self: {self}")
        return Base.to_json(self, ["password", "date_created"])
