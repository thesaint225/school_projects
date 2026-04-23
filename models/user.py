from extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)

    fullname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    dob = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    role = db.Column(db.String(20),nullable=False,default='student')

    