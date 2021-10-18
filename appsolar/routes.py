from appsolar import app
from flask import render_template

@app.route('/')
@app.route('/home')
def landing_page():
    return render_template('landing_page.html')