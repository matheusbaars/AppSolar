from appsolar import app
from flask import render_template, url_for, request, url_for, flash, redirect
from appsolar.models import Client
from appsolar import db

@app.route('/')
@app.route('/home')
def landing_page():
    return render_template('landing.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/clients')
def clients():
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        adress = request.form['adress']

        data = Client(name, surname, email, phone, adress)
        db.session.add(data)
        db.session.commit()
        flash('Client added successfully')
        return redirect(url_for('clients'))
    return render_template('clients.html')

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    client = Client.query.get(id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully')
    return redirect(url_for('clients'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    
    if request.method == 'POST':
        data = Client.query.get(request.form.get('id'))
        data.name = request.form['name']
        data.surname = request.form['surname']
        data.email = request.form['email']
        data.phone = request.form['phone']
        data.adress = request.form['adress']

        db.session.commit()
        flash('Client update successfully')
        return redirect(url_for('clients'))

