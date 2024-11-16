# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    membership_Id = db.Column(db.Integer, nullable=True)
   
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'membership_Id': self.membership_Id
        }