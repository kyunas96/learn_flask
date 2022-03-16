from utils.util import db

class Follow(db.model):
  id = db.column(db.Integer, primary_key=True)