from appsolar import app
from flask import render_template, url_for, request, url_for, flash, redirect
from appsolar.models import Client, Module, User
from appsolar import db

@app.route('/')
@app.route('/home')
def landing_page():
    return render_template('landing.html')

####################CLIENTS########################
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
####################CLIENTS########################

####################Simple Calculator##############
@app.route('/simplecalculator')
def simple_calculator():
    return render_template('simpleCalculator.html')
####################Simple Calculator##############

####################MODULES########################
@app.route('/modules')
def modules():
    modules = Module.query.all()
    return render_template('modules.html', modules=modules)

@app.route('/insertmodules', methods=['POST'])
def insertmodules():
    if request.method == 'POST':
        manufacture = request.form['manufacture']
        pmax = request.form['pmax']
        coefTempVoc = request.form['coefTempVoc']
        tempOpNom = request.form['tempOpNom']
        coefTempPmax = request.form['coefTempPmax']
        tolerancia = request.form['tolerancia']
        vma = request.form['vma']
        ima = request.form['ima']
        voc = request.form['voc']
        isc = request.form['isc']
        eficiencia = request.form['eficiencia']
            
        data = Module(manufacture, coefTempVoc, tempOpNom, coefTempPmax, pmax, tolerancia, vma, ima, voc, isc, eficiencia)
        db.session.add(data)
        db.session.commit()
        flash('Module added successfully')
        return redirect(url_for('modules'))
    return render_template('modules.html')

@app.route('/deletemodule/<id>')
def deletemodule(id):
    module = Module.query.get(id)
    db.session.delete(module)
    db.session.commit()
    flash('Module deleted successfully')
    return redirect(url_for('modules'))

@app.route('/updatemodule', methods=['GET', 'POST'])
def updatemodule():
    
    if request.method == 'POST':
        data = Module.query.get(request.form.get('id'))
        data.manufacture = request.form['manufacture']
        data.coefTempVoc = request.form['coefTempVoc']
        data.tempOpNom = request.form['tempOpNom']
        data.pmax = request.form['pmax']
        data.tolerancia = request.form['tolerancia']
        data.vma = request.form['vma']
        data.ima = request.form['ima']
        data.isc = request.form['isc']
        data.eficiencia = request.form['eficiencia']

        db.session.commit()
        flash('Module update successfully')
        return redirect(url_for('modules'))
    return render_template('modules.html')
####################MODULES########################

