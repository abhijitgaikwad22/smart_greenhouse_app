"""
Authentication routes module.
Handles login, logout, and session management.
"""

from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint('auth', __name__)

# Default credentials
DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'admin123'

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:

            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    """Handle user logout"""
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/index')
def index():
    """Landing page"""
    return render_template('index.html')
