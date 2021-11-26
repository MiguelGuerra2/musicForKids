from flask import (Blueprint, g, redirect, render_template, request, url_for)
from .auth import login_required
from .db import get_db

bp = Blueprint('MFKroutes',__name__)

@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        'select c.curse_name, u.name as teachername, cr.progress, cr.enrolled_at'
        ' from cursesregister cr INNER JOIN user u2 on cr.enrolled_user = u2.id'
        ' INNER JOIN curses c on cr.curse = c.id INNER JOIN user u on u.id = c.teacher'
        ' where cr.enrolled_user = %s order by enrolled_at desc',
        (g.user['id'],)
    )
    curses = c.fetchall()
    c.execute(
        'select n.notification, c.curse_name, un.not_check'
        ' from usersnotifications un INNER JOIN notifications n on un.not_name = n.id'
        ' INNER JOIN curses c on un.curse_from = c.id'
        ' where un.not_user = %s order by not_date desc',
        (g.user['id'],)
    )
    notifications = c.fetchall()
    return render_template('musicFK/index.html', curses=curses, notifications=notifications, name=g.user['name'])

@bp.route('/pruebalesson')
@login_required
def pruebita():
    db, c = get_db()
    c.execute(
        'select n.notification, c.curse_name, un.not_check'
        ' from usersnotifications un INNER JOIN notifications n on un.not_name = n.id'
        ' INNER JOIN curses c on un.curse_from = c.id'
        ' where un.not_user = %s order by not_date desc',
        (g.user['id'],)
    )
    notifications = c.fetchall()
    return render_template('musicFK/lessonview.html',notifications=notifications, name=g.user['name'])


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

#Ruta de cursos
@bp.route('/courses')
@login_required
def courses():
    return render_template('musicFK/courses.html')

#Para eliminar cursos a los que esta inscrito
@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    db, c = get_db()
    c.execute('delete from musicFK where id = %s and created_by = %s', (id, g.user['id']))
    db.commit()
    return redirect(url_for('musicFK.index'))

#Ruta de edición de cursos
@bp.route('/your-class')
def your_class():
    return render_template('musicFK/edit-course.html')