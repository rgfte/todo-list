from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from todo_bp.blueprint import todo

# DATABASE = 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ytpyfqrf123!@127.0.0.1:3306/todo'
db = SQLAlchemy(app)


app.register_blueprint(todo, url_prefix='/todo')


class todomod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complite = db.Column(db.Boolean)

    # def __repr__ (self):
    #     return '<todomod %r>' % self.id

# with app.app_context():
#     db.create_all()


@app.route('/')
def index():


    todos = todomod.query.all() 


    return render_template('index.html', todos=todos)



@app.route('/add', methods=['POST'])
def add():


    todo =  todomod(text=request.form['todo_item'], complite=False)
    db.session.add(todo)
    db.session.commit()


    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def update():


    todo = request.form.getlist('todo_check')
    for todo_check in todo: 
        item = todomod.query.get(todo_check) 
        db.session.delete(item)
        db.session.commit()


    return redirect(url_for('index'))


@app.route('/<int:id>')
def test(id):


    test = todomod.query.get_or_404(id)


    return render_template('test.html', test=test)


@app.route('/<int:id>/del')
def test_delete(id):


    delete = todomod.query.get_or_404(id)

    try: 
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'oops, error'
    

@app.route('/<int:id>/upd', methods=['POST', 'GET'])
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


@app.route('/newlist', methods=['POST'])
def newlist():

    return redirect(url_for('newlist'))