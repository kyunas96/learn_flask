from venv import create
from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import bcrypt

class User(Base):
  __tablename__= 'users'
  id = Column('user_id', Integer, primary_key=True)
  username = Column('username', String(32), nullable=False, unique=True)
  email = Column('email', String(64), nullable=False, unique=True)
  password = Column('password', String(), nullable=False)
  location = Column('location', String(128), nullable=True)
  bio = Column('bio', String(256), nullable=True)

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