from appsolar import app
from flask import render_template, url_for

@app.route('/')
@app.route('/home')
def landing_page():
    return render_template('landing.html')