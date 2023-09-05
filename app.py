from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity,
)
from datetime import date
from dotenv import load_dotenv
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['']
db = SQLAlchemy(app=app)
migrate = Migrate(app, db)
jwt=JWTManager
load_dotenv()


class Usuario(db.Model):
    __tablename__= 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False) 

    
class Entrada(db.Model):
    __tablename__= 'entrada'

    id_entrada = db.Column(db.Integer, primary_key=True)
    titulo_entrada = db.Column(db.String(100), nullable=False)
    contenido_entrada = db.Column(db.String(300), nullable=False)
    fecha_entrada = db.Column(db.Date, nullable=False)
    
    autor_entrada = db.Column(
        db.Integer,
        ForeignKey('usuario.id_usuario'),
        nullable=False
    )
    
 
class Comentario(db.Model):
    __tablename__= 'comentario'

    id_comentario = db.Column(db.Integer, primary_key=True)
    texto_comentario = db.Column(db.String(300), nullable=False)
    fecha_comentario = db.Column(db.Date, nullable=False)
    autor_comentario = db.Column(
        db.Integer,
        ForeignKey('usuario.id_usuario'),
        nullable=False
    )
    
    
class Categoria(db.Model):
    __tablename__= 'categoria'

    id_categoria = db.Column(db.Integer, primary_key=True)
    etiqueta_categoria = db.Column(db.String(100), nullable=False)

    
@app.context_processor
def set_mensaje():
    mensaje = "Blogger"
    return dict(
        mensaje = mensaje
    )

@app.route('/')
def index():
    print(os.environ)
    return render_template(
        'index.html',
    )

@app.route('/inicio')
def inicio():
    
    entradas = Entrada.query.all()
    return render_template(
        'inicio.html',
        entradas=entradas    
    )

@app.route('/agregar', methods=['POST'])
def agregar_entrada():
    contenido = request.form['contenido']
    fecha = date.today()
    entrada= Entrada(titulo_entrada=contenido, contenido_entrada=contenido, fecha_entrada=fecha, autor_entrada=1)
    db.session.add(entrada)

    db.session.commit()

    return redirect(
        url_for('inicio')
    )
 
@app.route('/agregar_usuario', methods=['post']) #colocar en el boton registrar
def agregar_usuario():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    password_hasheada = generate_password_hash(
        password=password,
        method="pbkdf2",
        salt_length=8
    )

    mail = data.get('mail')

    nuevo_usuario = Usuario(
        nombre_usuario=username,
        correo_electronico=mail,
        password_hash=password_hasheada
    )
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"Mensaje":"Usuario creado correctamente"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    usuario = Usuario.query.filter_by(username=usuario).first()

    if usuario and check_password_hash(
        usuario.password_hash, password):
        access_token = create_access_token(
            identity=usuario.username,
            expires_delta=timedelta(seconds=30)

        )
        return {"OK":"Usuario logueado",
            "Token":access_token }
    return{"Error", "Usuario o contraseña incorrecta"}
    
