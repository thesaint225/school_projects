# let me work with databases instead of raw sql
from flask_sqlalchemy import SQLAlchemy
# this give the user class login features automatically
from flask_login import UserMixin

# connection between flask and the database 
db = SQLAlchemy()

# creating a database table called User
class User (db.Model,UserMixin):
    # every user get a unique Id
    id = db.Column(db.Integer,primary_key=True)

    username= db.Column(db.String(100),unique=True,nullable=False)

    existing_user= user.query.filter_by(username=username).first()
    if existing_user:
        return "userName already exists"

     # 🔐 store hashed password (NOT plain password)
     password_hash = db.Column(db.String(200),nullable=False)
    # admin,teacher,student
     role=db.Column(db.string(20),nullable=False) 
