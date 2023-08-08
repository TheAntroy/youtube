from app import app, db
from flask import render_template, request, redirect, url_for
from .forms import TodoForm
from .models import TodoList

@app.route('/', methods=['get','post'])
def home():
    form = TodoForm()
    if request.method == 'POST':
        data = request.form['todo']
        dataUp = TodoList(data)
        db.session.add(dataUp)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', form=form, data=TodoList.query.all(), judul='Flask | To-Do-List')


@app.route('/edit/<id>', methods=['POST','GET'])
def edit(id):
    form = TodoForm()
    editTodo = TodoList.query.filter_by(id=id).first()
    if request.method == 'POST':
        editTodo.mytodolist = request.form['todo']
        db.session.add(editTodo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', form=form, editTodo=editTodo, edit='test', data=TodoList.query.all())


@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    data = TodoList.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('home'))


