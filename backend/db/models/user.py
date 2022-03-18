from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class User(Base):
  __tablename__= 'users'
  id = Column('user_id', Integer, primary_key=True)
  username = Column('username', String(32))
  email = Column('email', String(64))

  def __init__(self, username, email):
    if not username or not email:
      raise Exception('Missing fields for User instance')
    self.username = username
    self.email = email

    
