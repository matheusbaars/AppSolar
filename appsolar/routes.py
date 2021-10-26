from sqlalchemy.orm.base import MANYTOONE
from appsolar import app
from flask import render_template, url_for, request, url_for, flash, redirect, get_flashed_messages
from appsolar.forms import RegisterForm, LoginForm
from appsolar.models import Client, Module, User, Irradiacao
from appsolar import db
from appsolar.functions import *
from flask_login import login_user, logout_user, login_required


####################LOGIN########################
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def landing_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()             
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):            
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category='success')
            return redirect(url_for('services'))
        else:
            flash(f'Username and password are not match! Please try again', category='danger')
    return render_template('landing.html', form=form)
####################LOGIN########################

####################LOGOUT########################
@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('landing_page'))
####################LOGOUT########################

####################CLIENTS########################
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adress = form.email_adress.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully. You are logged in as {user_to_create.username}', category='success')

        return redirect(url_for('services'))
    if form.errors != {}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/clients')
@login_required
def clients():
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/insert', methods=['POST'])
@login_required
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
@login_required
def delete(id):
    client = Client.query.get(id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully')
    return redirect(url_for('clients'))

@app.route('/update', methods=['GET', 'POST'])
@login_required
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
@login_required
def simple_calculator():
    modules = Module.query.all()
    irradiations = Irradiacao.query.all()
    return render_template('simpleCalculator.html',  irradiations=irradiations, modules=modules)

@app.route('/simplecalculate', methods=['GET', 'POST'])
@login_required
def simplecalculate():
    meanconsume = request.form['meanconsume']
    custodisponibilidade = request.form['custodisponibilidade']
    module_data = request.form['modules']
    irradiation_data = request.form['irradiation']
    losses = request.form['losses']
    #for key, value in request.form.items():
    #    print("key: {0}, value: {1}".format(key, value))
    id = module_data[-1]
    id_irr = irradiation_data[-1]    
    module_data = Module.query.filter_by(id=id).first()
    irradiation_data = Irradiacao.query.filter_by(id=id_irr).first()
    custodisponibilidade = costOfDisponibility(custodisponibilidade)
    net_energy = monthlyEnergyConsumedLessCostDisponibility(meanconsume, custodisponibilidade)
    net_energy_per_day = net_energy / 30
    power_peak = net_energy_per_day / float(irradiation_data.irr_media)
    number_modules = power_peak * 1000 / float(module_data.pmax)
    energy_produced_no_loss =  power_peak * float(irradiation_data.irr_media) * 30 * (1 - (float(losses) / 100))
    return render_template('results_simple_calculator.html', number_modules=number_modules, custodisponibilidade=custodisponibilidade, meanconsume=meanconsume, power_peak=power_peak, module_data=module_data, irradiation_data=irradiation_data, energy=energy_produced_no_loss)    
####################Simple Calculator##############

####################MODULES########################
@app.route('/modules')
@login_required
def modules():
    modules = Module.query.all()
    return render_template('modules.html', modules=modules)

@app.route('/insertmodules', methods=['POST'])
@login_required
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
@login_required
def deletemodule(id):
    module = Module.query.get(id)
    db.session.delete(module)
    db.session.commit()
    flash('Module deleted successfully')
    return redirect(url_for('modules'))

@app.route('/updatemodule', methods=['GET', 'POST'])
@login_required
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
@login_required
def irradiation():
    irradiations = Irradiacao.query.all()
    return render_template('irradiation.html', irradiations=irradiations)

@app.route('/insertcityirradiation', methods=['POST'])
@login_required
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
@login_required
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
@login_required
def deleteirradiation(id):
    irradiation = Irradiacao.query.get(id)
    db.session.delete(irradiation)
    db.session.commit()
    flash('City irradiation deleted successfully')
    return redirect(url_for('irradiation'))
####################IRRADIAÇÃO#####################

####################SERVICES#####################
@app.route('/services')
@login_required
def services():
    return render_template('services.html')
####################SERVICES#####################
