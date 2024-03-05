from flask import Flask, g
from flask import render_template, redirect, url_for, request, Blueprint
from flask_sqlalchemy import SQLAlchemy

todo = Blueprint('todo',  __name__, template_folder='templates')

db = None


@todo.before_request
def before_request():
     global db
     db = g.get('')


@todo.teardown_request
def teardown_request(request):
    global db
    db = None
    return request


@todo.route('/')
def index():


    todos = query.all() 


    return render_template('index.html', todos=todos)


@todo.route('/add', methods=['POST'])
def add():


    todo =  todomod(text=request.form['todo_item'], complite=False)
    db.session.add(todo)
    db.session.commit()


    return redirect(url_for('index'))


@todo.route('/delete', methods=['POST'])
def update():


    todo = request.form.getlist('todo_check')
    for todo_check in todo: 
        item = todomod.query.get(todo_check) 
        db.session.delete(item)
        db.session.commit()


    return redirect(url_for('index'))


@todo.route('/<int:id>')
def test(id):


    test = todomod.query.get_or_404(id)


    return render_template('test.html', test=test)


@todo.route('/<int:id>/del')
def test_delete(id):


    delete = todomod.query.get_or_404(id)

    try: 
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'oops, error'
    

@todo.route('/<int:id>/upd', methods=['POST', 'GET'])
def test_update(id):

    todo = todomod.query.get(id)
    if request.method == 'POST':
        todo.text = request.form.get('text')

        try: 
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return'oops, error'
    return render_template('update.html', todo=todo)