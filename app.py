from flask import Flask
from extensions import db
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():

    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # import blueprints
    from routes.auth_routes import auth_bp
    from routes.student_routes import student_bp
    
    from routes.teacher_routes import teacher_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(teacher_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)