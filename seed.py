from app import create_app
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash

app = create_app()
def seed_data():
    with app.app_context():
        existing = User.query.filter_by(username='teacher').first()

        if not existing:
            teacher = User(
            fullname = "kwame Mensah",
            email = 'kwamemenasah@gmail.com',
            username='teacher1',
            password_hash=generate_password_hash('teacher123'),
            role='teacher'
            )

            db.session.add(teacher)
            db.session.commit()
            print("Teacher created")
        else:
            print("Teacher already exists")

        
        


# if__name__ =="__main__":
# seed_data()

if __name__ == "__main__":
    seed_data()
