"""
Main Flask application entry point.
Only handles app initialization and blueprint registration.
No business logic here.
"""

from flask import Flask, render_template, request, redirect, url_for, session
from routes.auth_routes import auth_bp
from routes.detection_routes import detection_bp
from routes.dashboard_routes import dashboard_bp
import os


def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY',
                                    'dev-secret-key-change-in-production')

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(detection_bp)
    app.register_blueprint(dashboard_bp)

    # ✅ Global Login Protection
    @app.before_request
    def require_login():

        if not request.endpoint:
            return

        allowed_routes = [
            'root',
            'about',
            'auth.login',
            'auth.index',
            'static'
        ]

        if request.endpoint not in allowed_routes and not session.get('logged_in'):
            return redirect(url_for('auth.login'))

    # Root route
    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/sample1')
    def sample1():
        return render_template('sample1.html')

    @app.route('/sample2')
    def sample2():
        return render_template('sample2.html')

    @app.route('/crop-guide')
    def crop_guide():
        return render_template('crop_guide.html')

    @app.route('/weather-advisory')
    def weather_advisory():
        return render_template('weather_advisory.html')

    @app.route('/crop-comparison')
    def crop_comparison():
        return render_template('crop_comparison.html')

    @app.route('/crop-recommendation')
    def crop_recommendation():
        return render_template('crop_recommendation.html')

    # ✅ About Page → No Login Required
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/fertilizer-guide')
    def fertilizer_guide():
        return render_template('fertilizer_guide.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)