# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'start_date': self.start_date,
            'expiry_date': self.expiry_date
        }