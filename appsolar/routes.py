from sqlalchemy.orm.base import MANYTOONE
from appsolar import app
from flask import render_template, url_for, request, url_for, flash, redirect, jsonify
from appsolar.models import Client, Module, User, Irradiacao
from appsolar import db
from appsolar.functions import *


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
    modules = Module.query.all()
    return render_template('simpleCalculator.html', modules=modules)

@app.route('/simplecalculate', methods=['GET', 'POST'])
def simplecalculate():
    meanconsume = request.form['meanconsume']
    custodisponibilidade = request.form['custodisponibilidade']
    module_data = request.form['modules']

    #for key, value in request.form.items():
    #    print("key: {0}, value: {1}".format(key, value))
    id = module_data[-1]
    module_data = Module.query.filter_by(id=id).first()
    
    
    custodisponibilidade = costOfDisponibility(custodisponibilidade)
    net_energy = monthlyEnergyConsumedLessCostDisponibility(meanconsume, custodisponibilidade)
    net_energy_per_day = net_energy / 30
    return f'Calculado{net_energy_per_day} | {module_data.pmax}'
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

####################IRRADIAÇÃO#####################
@app.route('/irradiation')
def irradiation():
    irradiations = Irradiacao.query.all()
    return render_template('irradiation.html', irradiations=irradiations)

@app.route('/insertcityirradiation', methods=['POST'])
def insertcityirradiation():
    if request.method == 'POST':
        city = request.form['irr-city']
        january = request.form['irr-january']
        february = request.form['irr-february']
        march = request.form['irr-march']
        april = request.form['irr-april']
        may = request.form['irr-may']
        june = request.form['irr-june']
        july = request.form['irr-july']
        august = request.form['irr-august']
        september = request.form['irr-september']
        october = request.form['irr-october']
        november = request.form['irr-november']
        december = request.form['irr-december']
        mean = request.form['irr-mean']

        data = Irradiacao(city, january, february, march, april, may, june, july, august, september, october, november, december, mean)
        db.session.add(data)
        db.session.commit()
        flash('City irradiation added successfully')
        return redirect(url_for('irradiation'))
    return render_template('irradiation.html')

@app.route('/updateirradiation', methods=['GET', 'POST'])
def updateirradiation():
    if request.method == 'POST':
        data = Irradiacao.query.get(request.form.get('id'))
        data.irr_cidade = request.form['irr-city']
        data.irr_janeiro = request.form['irr-january']
        data.irr_fevereiro = request.form['irr-february']
        data.irr_março = request.form['irr-march']
        data.irr_abril = request.form['irr-april']
        data.irr_maio= request.form['irr-may']
        data.irr_junho= request.form['irr-june']
        data.irr_julho = request.form['irr-july']
        data.irr_agosto = request.form['irr-august']
        data.irr_setembro = request.form['irr-september']
        data.irr_outubro = request.form['irr-october']
        data.irr_novembro = request.form['irr-november']
        data.irr_dezembro = request.form['irr-december']
        data.irr_media = request.form['irr-mean'] 

        db.session.commit()
        flash('City Irradiation update successfully')
        return redirect(url_for('irradiation'))
    return render_template('irradiation.html')

@app.route('/deleteirradiation/<id>')
def deleteirradiation(id):
    irradiation = Irradiacao.query.get(id)
    db.session.delete(irradiation)
    db.session.commit()
    flash('City irradiation deleted successfully')
    return redirect(url_for('irradiation'))
####################IRRADIAÇÃO#####################

