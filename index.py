import os # Permite acceder a variables de entorno
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY= 'mikey', #Llave que va a servir para poder definir las sesiones en la aplicacion.
    DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
    DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
    DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
    DATABASE=os.environ.get("FLASK_DATABASE"),
    SERIALIZER_KEY=os.environ.get("FLASK_SERIALIZER_KEY"),
    DUMPS_KEY=os.environ.get("FLASK_DUMPS_KEY"),
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USERNAME=os.environ.get("FLASK_EMAIL"),
    MAIL_PASSWORD=os.environ.get("FLASK_MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.environ.get("FLASK_EMAIL"),
    MAIL_USE_TLS= False,
    MAIL_USE_SSL=True
)

import db

db.init_app(app)

import auth
import MFKroutes

app.register_blueprint(auth.bp)
app.register_blueprint(MFKroutes.bp)
    


