print("LOADING TEACHER ROUTES")
from flask import Blueprint, session, redirect, url_for

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teacher')
def teacher_dashboard():

    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if session.get('role') != 'teacher':
        return "access denied", 403

    return f"Welcome {session['username']}"