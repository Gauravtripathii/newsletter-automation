from . import db
from sqlalchemy.sql import func

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String)
	date_added = db.Column(db.DateTime(timezone=True), default=func.now())