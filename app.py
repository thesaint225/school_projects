from flask import Flask,render_template,request,redirect,session,url_for
from sqlalchemy import text
import  os 
from werkzeug.security import generate_password_hash,check_password_hash
from models.user import User
from extensions import db

from dotenv import load_dotenv

# load environment variable from .env
load_dotenv()
app = Flask(__name__)

app.secret_key= os.getenv("SECRET_KEY")
# config the database first 
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# initialize db
db.init_app(app)


@app.route("/")
def home():
    return render_template('login.html')

# to handle authentication
@app.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")
    confirmed_password =request.form.get("confirm_password")
    role = request.form.get("role")

    # Basic validation 
    if not username or not password :
        return 'missing username or password',404
    
    #Fetch user using ORM(safe)
    user = User.query.filter_by(username=username).first()

    #invalid login
    if not user or not  check_password_hash(user.password_hash,password):
        return 'invalid credential',401
    
    # store session
    session['user_id']= user.id
    session['role']=user.role 
    session['username']=user.username

    # redirect based on role 
    if user.role == 'teacher':
        return redirect(url_for('teacher_dashboard'))
    
    elif user.role == 'student':
        return redirect(url_for('student'))
    
    return 'invalid role',403
       
    
    return 'invalid credential'

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')  

    # FORM DATA
    fullname= request.form.get('fullname')
    email=request.form.get('email')
    username=request.form.get('username')
    password=request.form.get('password')
    confirmed_password=request.form.get('confirm_password')
    dob=request.form.get('dob')
    gender=request.form.get('gender')
    department = request.form.get('department')

    # validation
    if not all([fullname,email,username,password,confirmed_password,]):
        return "missing field",400
    
    if password != confirmed_password:
        return 'password do no match',400

    
    hashed_password = generate_password_hash(password)

    # CREATE USER 
    new_user = User(
    fullname=fullname,
    email=email,
    username=username,
    password_hash = hashed_password,
    dob=dob,
    gender=gender,
    department=department,
    role="student"
)

    try:
        db.session.add(new_user)
        db.session.commit()
        return 'User registered successfully'
    

    except Exception as e :
        db.session.rollback()
        return f"Error:str{(e)}"


@app.route("/test")
def test():
    return "App is working"


@app.route("/db-test")
def db_test():
    try:
        result = db.session.execute(text("SELECT 1")).fetchone()
        return f"Database connected: {result}"
    except Exception as e:
        return f"Database error: {str(e)}"





@app.route('/teacher')
def teacher_dashboard():
    if 'user' not in session:
        return redirect("/")

    if session.get('role')!='teacher':
        return 'access denied'

    
    return f"welcome{session['user']}"


@app.route('/student_dashboard')
def student():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    

    if session.get('role') !='student':
        return 'access denied',403 
    

    return render_template('student.html')


@app.route('/logout')
def logout():
    session.clear()
    return "Logged out"




if __name__ == "__main__":
    app.run(debug=True)