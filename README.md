🎯 OBJECTIVE

Build a secure web-based system that allows:

Admin, Teacher, Student authentication
Role-based dashboards
Secure database operations (CRUD)
Strong security practices (like real systems)
🧩 CORE FEATURES
🔐 1. Authentication System (LOGIN + REGISTER)
👤 Roles:
Admin
Teacher
Student
🔑 Features:
Login page
Register page (Teacher & Student only)
Password hashing (SECURITY ✅)
Session management (Flask-Login)
Logout system

🛡️ Security Requirements
Passwords must be hashed (never plain text)
Prevent SQL Injection (use ORM)
Protect routes (@login_required)
Role-based access control (RBAC)

🧑‍💻 2. DASHBOARDS (UI)
🟣 Admin Dashboard
View all users
Add / delete users
Manage teachers & students
🔵 Teacher Dashboard
View assigned students
Add/update student records
🟢 Student Dashboard
View personal data
View grades (future feature)
🗄️ 3. DATABASE (SQL + CRUD)
🧱 Tables:
🔹 Users Table
Field Description
id Primary key
username Unique
password_hash Encrypted password
role admin / teacher / student
🔹 (Future) Student Table
Field Description
id Primary key
name Student name
class Class
teacher_id Linked teacher
🔄 CRUD OPERATIONS

✔ Create user (register)
✔ Read users (admin view)
✔ Update user info
✔ Delete user

⚙️ 4. SYSTEM ARCHITECTURE
├── app.py
├── models.py
├── requirements.txt
├── .env 🔐 (NEW - stores secrets)
├── .gitignore 🔐 ( IMPORTANT)
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── admin.html
│ ├── teacher.html
│ └── student.html
│
├── static/
│ └── style.css
│
├── instance/
│ └── app.db
│
└── venv/
🔐 5. SECURITY ENGINEERING FEATURES (IMPORTANT)
🛡️ Phase 1 (Now)
Password hashing
Login sessions
Role-based access
🔒 Phase 2 (Next)
Login attempt limits (brute force protection)
CSRF protection
Input validation
🔥 Phase 3 (Advanced)
JWT authentication
OAuth (Google login)
Secure cookies
HTTPS enforcement

# ⚙️ Installation Guide

Follow these steps to run the project locally:

## 1. Clone the project

```bash
git clone <your-repository-url>
cd school_system
```

## 2. Create virtual environment

```bash
python -m venv venv
```

## 3. Activate virtual environment (Windows PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the application

```bash
python app.py
```

## 6. Open in browser

Go to:
http://127.0.0.1:5000/
