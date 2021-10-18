import os # Permite acceder a variables de entorno
from flask import Flask
from dotenv import load_dotenv
def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_mapping(
        SECRET_KEY= 'mikey', #Llave que va a servir para poder definir las sesiones en la aplicacion.
        DATABASE_HOST=os.getenv("FLASK_DATABASE_HOST_1"),
        DATABASE_PASSWORD=os.getenv("FLASK_DATABASE_PASSWORD_1"),
        DATABASE_USER=os.getenv("FLASK_DATABASE_USER_1"),
        DATABASE=os.getenv("FLASK_DATABASE_DB"),
        SERIALIZER_KEY=os.getenv("FLASK_SERIALIZER_KEY"),
        DUMPS_KEY=os.getenv("FLASK_DUMPS_KEY"),
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USERNAME=os.getenv("FLASK_EMAIL"),
        MAIL_PASSWORD=os.getenv("FLASK_MAIL_PASSWORD"),
        MAIL_DEFAULT_SENDER=os.getenv("FLASK_EMAIL"),
        MAIL_USE_TLS= False,
        MAIL_USE_SSL=True
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import MFKroutes

    app.register_blueprint(auth.bp)
    app.register_blueprint(MFKroutes.bp)
    
    return app


