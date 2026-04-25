from flask import Blueprint, session, render_template, redirect, url_for,request

student_bp = Blueprint('student', __name__)

@student_bp.route('/student_dashboard')
def student_dashboard():

    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if session.get('role') != 'student':
        return "access denied", 403

    page = request.args.get('page', 'home')

    return render_template('student.html', page=page)