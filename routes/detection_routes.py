"""
Detection routes module.
Handles environment detection and analysis.
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from services.decision_engine import analyze_environment
from utils.csv_logger import save_detection, init_csv_if_not_exists
from services.export_service import export_to_pdf, export_history_csv
from functools import wraps
import os

detection_bp = Blueprint('detection', __name__)

def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@detection_bp.route('/detect', methods=['GET', 'POST'])
@login_required
def detect():
    """Environment detection page"""
    # Initialize CSV if it doesn't exist
    init_csv_if_not_exists()
    
    if request.method == 'POST':
        # Get form data
        crop = request.form.get('crop')
        temperature = float(request.form.get('temperature'))
        humidity = float(request.form.get('humidity'))
        soil_moisture = float(request.form.get('soil_moisture'))
        light = float(request.form.get('light'))
        
        # Analyze environment using decision engine
        analysis_result = analyze_environment(
            crop, temperature, humidity, soil_moisture, light
        )
        
        # Save to CSV
        save_detection(
            crop, temperature, humidity, soil_moisture, light,
            analysis_result['status'], analysis_result['score']
        )
        
        return render_template('detect.html', 
                             result=analysis_result,
                             form_data=request.form)
    
    return render_template('detect.html', result=None)

@detection_bp.route('/export/pdf', methods=['POST'])
@login_required
def export_pdf():
    """Export detection result as PDF"""
    data = request.get_json()
    pdf_output = export_to_pdf(data)
    return pdf_output

@detection_bp.route('/export/csv')
@login_required
def export_csv():
    """Export history as CSV"""
    return export_history_csv()