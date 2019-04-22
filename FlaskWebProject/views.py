"""
Routes and views for the flask application.
"""

from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('Project.html')
