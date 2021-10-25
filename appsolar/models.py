from appsolar import db
from appsolar import bcrypt

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=100))
    email = db.Column(db.String(length=100), unique=True, nullable=False)
    phone = db.Column(db.String(length=12))
    adress = db.Column(db.String())

    def __init__(self, name,surname, email, phone, adress):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.adress = adress

    def __repr__(self):
        return f'Name {self.name}'

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_adress = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(length=50), nullable=False)
    coefTempVoc = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    tempOpNom = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    coefTempPmax = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    pmax = db.Column(db.Integer, nullable=False)
    tolerancia = db.Column(db.Float(precision=2, asdecimal=True))
    vma = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    ima = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    voc = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    isc = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    eficiencia = db.Column(db.Float(precision=2, asdecimal=True))

    def __init__(self, manufacture, coefTempVoc,tempOpNom, coefTempPmax, pmax, tolerancia, vma, ima, voc, isc, eficiencia):
        self.manufacture = manufacture
        self.coefTempVoc = coefTempVoc
        self.tempOpNom = tempOpNom
        self.coefTempPmax = coefTempPmax
        self.pmax = pmax
        self.tolerancia = tolerancia
        self.vma = vma
        self.ima = ima
        self.voc = voc
        self.isc = isc
        self.eficiencia = eficiencia

class Irradiacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    irr_cidade = db.Column(db.String(length=50),nullable=False, unique=True)
    irr_janeiro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_fevereiro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_março = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_abril = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_maio = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_junho = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_julho = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_agosto = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_setembro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_outubro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_novembro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_dezembro = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    irr_media = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)

    def __init__(self, irr_cidade, irr_janeiro, irr_fevereiro, irr_março, irr_abril, irr_maio, irr_junho, irr_julho, irr_agosto, irr_setembro, irr_outubro, irr_novembro, irr_dezembro, irr_media):
        self.irr_cidade = irr_cidade
        self.irr_janeiro = irr_janeiro
        self.irr_fevereiro = irr_fevereiro
        self.irr_março = irr_março
        self.irr_abril = irr_abril
        self.irr_maio = irr_maio
        self.irr_junho = irr_junho
        self.irr_julho = irr_julho
        self.irr_agosto = irr_agosto
        self.irr_setembro = irr_setembro
        self.irr_outubro = irr_outubro
        self.irr_novembro = irr_novembro
        self.irr_dezembro = irr_dezembro
        self.irr_media = irr_media
        