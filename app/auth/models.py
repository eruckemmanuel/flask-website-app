# Import the database object (db) from the main application module
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# User model
class User(Base):

    __tablename__ = 'auth_user'

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status  = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, email, password, role, status,
                 first_name=None, last_name=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role,
        self.status = status

    def __repr__(self):
        return '<User %r>' % (self.email)  