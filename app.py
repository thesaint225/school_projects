from flask import Flask,render_template,request,redirect,session
from sqlalchemy import text
import  os 
from werkzeug.security import generate_password_hash
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

# print(os.getenv('DATABASE_URL'))

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
    role = request.form.get("role")    
    
    # replace with database later 
    if username == "admin" and password == "1234":
        session["user"] =username
        session['role'] ="teacher"
        return redirect('/teacher')       
    
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
    hashed_password= generate_password_hash(password)

    # CREATE USER 
    new_user = User(
    fullname=fullname,
    email=email,
    username=username,
    password_hash = hashed_password,
    dob=dob,
    gender=gender,
    department=department
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

# @app.route('/dashboard')
# def dashboard():
#     if "user" not in session:
#         return redirect('/login')
#     return f'Welcome {session['user']} to the dashboard'



@app.route('/teacher')
def teacher_dashboard():
    if 'user' not in session:
        return redirect("/")

    if session.get('role')!='teacher':
        return 'access denied'

    
    return f"welcome{session['user']}"


@app.route('/logout')
def logout():
    session.clear()
    return "Logged out"




if __name__ == "__main__":
    app.run(debug=True)