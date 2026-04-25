from flask import Blueprint, request, render_template, redirect, session, url_for
from werkzeug.security import generate_password_hash
from models.user import User
from extensions import db
from services.auth_service import authenticate_user

auth_bp = Blueprint('auth',__name__)

# login
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get ('password')

    if not username or not password :
        return 'missing username or password',400

    user= authenticate_user(username,password)

    if not user:
        return 'invalid credentials', 401

    session['user_id'] = user.id 
    session['role'] = user.role
    session['username'] = user.username

    if user.role == "teacher":
        return redirect(url_for('teacher.teacher_dashboard'))
    
    return redirect(url_for('student.student_dashboard'))

# register 
@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    

    fullname = request.form.get('fullname')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    department = request.form.get('department')

    if not all([fullname, email, username, password, confirm_password]):
        return "missing field", 400
    
    if password != confirm_password:
        return "password do not match", 400
    
    hashed_password = generate_password_hash(password)


    new_user = User(
        fullname=fullname,
        email=email,
        username=username,
        password_hash=hashed_password,
        dob=dob,
        gender=gender,
        department=department,
        role="student"
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return "User registered successfully"

    except Exception as e:
        db.session.rollback()
        return str(e), 500


# logout 


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))





