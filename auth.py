import functools
import click
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect, current_app
)
from flask.cli import with_appcontext
from flask_mail import Mail, Message
from itsdangerous.exc import SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from db import get_db
from itsdangerous import URLSafeTimedSerializer


bp = Blueprint('auth', __name__, url_prefix='/auth')



@with_appcontext
@bp.route('/register', methods=['GET', 'POST'])
def register(k=0):
    s = URLSafeTimedSerializer(current_app.config['SERIALIZER_KEY'])
    mail = Mail(current_app)
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        tel = request.form['tel']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        error = None
        session['username'] = username
        session['email'] = email
        session['tel'] = tel
        session['password'] = pass1
        db, c = get_db()
        c.execute(
            'select id from user where email = %s', (email,)
        )
        if not username:
            error = 'Username es requerido'
        if not pass1:
            error = 'Password es requerido'
        if not pass2:
            error = 'Confirmacion de password requerida'
        if pass1 != pass2:
            error = 'Las contrasenas deben coincidir'
        elif c.fetchone() is not None:
            error = 'Email ingresado ya se encuentra registrado.'.format(g.email)
        
        if error is None:
            token = s.dumps(email, salt=current_app.config['DUMPS_KEY'])
            htmltext = ['Solicitud Exitosa','Se ha enviado le ha enviado un mensaje de confirmacion a la direccion de correo electronico ingresada.']
            msg = Message('Correo de confirmacion', recipients=[email])
            link = url_for('auth.confirm_email', token=token, _external=True)
            name = username.split()
            name1 = name[0]
            msg.html = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                        </head>
                        <body style="background-color: #ffffff;">
                            <div style="width: 100%; height: 50px; background-color: #600395;"></div>
                            <h1 style="text-align: center;"><b>Hola, {}</b></h1>
                            <p style="text-align: center;">Estas a solo un paso de ser parte del equipo Music For Kids.</p>
                            <p style="text-align: center;">Presiona el siguiente boton para confirmar tu correo:</p>
                            <div style="display: flex; flex-direction: column;">
                                <a href="{}" style="background-color: #600395;color: white; padding: 8px; text-decoration: none; margin: 50px auto;"><b>Confirmar Email</b></a> <br>
                            </div>
                        </body>
                        </html>
                       """.format(name1, link)
            mail.send(msg)
            return render_template('auth/confirm.html', htmltext=htmltext)
        return render_template('auth/register.html', error=error)    
    return render_template('auth/register.html')

@with_appcontext
@bp.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):
    s = URLSafeTimedSerializer(current_app.config['SERIALIZER_KEY'])
    try:
        emailtest= s.loads(token, salt=current_app.config['DUMPS_KEY'], max_age=1800)
    except SignatureExpired:
        htmltext = ['Lo sentimos, ha ocurrido un error','El link de confirmacion expiro.','Para crear su cuenta repita el proceso de registro.','registro']
        return render_template('auth/confirm.html', htmltext=htmltext)
    username=session['username']
    email=session['email']
    tel=session['tel']
    password=session['password']
    db, c = get_db()
    c.execute(
                'insert into user (name, email, tel, password, user_type) values (%s,%s,%s,%s,3)',
                (username,email,tel,generate_password_hash(password))
            )
    db.commit()
    htmltext = ['Felicitaciones','Su cuenta ha sido activada exitosamente']
    return render_template('auth/confirm.html', htmltext=htmltext)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select * from user where email = %s', (email,)
        )
        user = c.fetchone()
        if user is None:
             error = 'Usuario y/o contrasena invalida'
        elif not check_password_hash(user['password'], password):
             error = 'Usuario y/o contrasena invalida'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('MFKroutes.index'))
            
        return render_template('auth/login.html', error=error)    

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from user where id = %s', (user_id,)
        )
        g.user = c.fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrap_view(**kwargs):
        if g.user is None:
            flash('Para acceder a esta URL primero debes iniciar sesion', 'warning')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrap_view

@bp.route('/logout')
def logout():
    session.clear()
    flash('Esperamos que vuelvas pronto', 'success')
    return redirect(url_for('auth.login'))