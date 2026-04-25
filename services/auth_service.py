from werkzeug.security import generate_password_hash,check_password_hash
from models.user import User

def authenticate_user(username,password):
    user= User.query.filter_by(username=username).first()

    if not user:
        return None
    
    if not check_password_hash(user.password_hash,password):
        return None
    
    return user