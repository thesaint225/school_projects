from flask import Flask,render_template,request,redirect,session
import  os 
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.secret_key= os.getenv("SECRETS_KEY")




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
    return render_template('register.html')


@app.route("/test")
def test():
    return "App is working"

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