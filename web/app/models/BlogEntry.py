from app import db
from sqlalchemy_serializer import SerializerMixin


class BlogEntry(db.Model , SerializerMixin):
    __tablename__ = "blog_entries"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    date_created = db.Column(db.String(50))
    date_updated = db.Column(db.String(50))

    def __init__(self, name, message, email,date_created, date_updated):
        self.name = name
        self.message = message
        self.email = email
        self.date_created = date_created
        self.date_updated = date_updated

    def update(self, name, message, email, date_created, date_updated):
        self.name = name
        self.message = message
        self.email = email
        self.date_created = date_created
        self.date_updated = date_updated
