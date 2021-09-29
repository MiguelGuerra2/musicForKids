from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from auth import login_required
from db import get_db

bp = Blueprint('MFKroutes',__name__)

@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        'select c.curse_name, u.name as teachername, cr.completed, cr.enrolled_at'
        ' from cursesregister cr INNER JOIN user u2 on cr.enrolled_user = u2.id'
        ' INNER JOIN curses c on cr.curse = c.id INNER JOIN user u on u.id = c.teacher'
        ' where cr.enrolled_user = %s order by enrolled_at desc',
        (g.user['id'],)
    )
    curses = c.fetchall()
    return render_template('musicFK/index.html', curses=curses, name=g.user['name'])

@bp.route('/enrollcurse', methods=['GET', 'POST'])
@login_required
def enroll():
    # if request.method == 'POST':
        #Aqui se incribiran a los cursos
        #nombre del curso o ID (me parece mejor este ultimo)
        # namecurse = 'Curso de Guitarra: Avanzado'
        # #usuario inscrito se obtiene de variable global
        # #completed -> Booleano para saber si se completo el curso
        # db, c = get_db()
        # c.execute(
        #     'insert into cursesregister (namecurse, enrolled_user, completed)'
        #     ' values (%s, %s, %s)',
        #     (namecurse, g.user['id'], False)
        # )
        # db.commit()
        # return redirect(url_for('musicFK.index'))

    return render_template('musicFK/enroll.html')

#Para eliminar cursos a los que esta inscrito
@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    db, c = get_db()
    c.execute('delete from musicFK where id = %s and created_by = %s', (id, g.user['id']))
    db.commit()
    return redirect(url_for('musicFK.index'))