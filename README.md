├── app.py
├── config.py

├── models/
│ ├── **init**.py ✅ (IMPORTANT - makes models a package)
│ ├── user.py
│ ├── student.py
│ └── teacher.py

├── services/
│ ├── auth_service.py
│ └── user_service.py

├── routes/
│ ├── auth_routes.py
│ ├── admin_routes.py
│ ├── teacher_routes.py
│ └── student_routes.py

├── templates/
│ ├── login.html
│ ├── register.html
│ ├── admin.html
│ ├── teacher.html
│ └── student.html

├── static/
│ └── style.css

├── instance/
│ └── app.db (optional local dev)

├── .env
├── .gitignore
├── requirements.txt
└── venv/
