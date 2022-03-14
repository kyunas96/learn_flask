from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Follow(db.model):
  id = db.column