import mysql.connector

import click #Sirve para ejecutar comandos en la terminal
from flask import config, current_app, g #Mantiene la aplicacion ejecutandose y g permite almacenar variables
from flask.cli import with_appcontext #Permite acceder a las variables de la configuracion de la aplicacion
from schema import instructions #Carpeta creada 

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'], #Se usa corchetes porque son propiedades de la configuracion
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None): #Funcion para cerrar el cursor despues de consultas
    db = g.pop('db', None) #quitamons propiedad
    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    db.commit()

@click.command('init-db') #Para ejecutar esta funcion se debe escribir en la consola: flask init-db
@with_appcontext

def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db) #Ejecutar funciones cuando se termina de ejecutar la app
    app.cli.add_command(init_db_command)


