from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

todo_list = []

class TaskForm(Form):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm(request.form)
    if request.method == 'POST' and form.validate():
        todo_list.append(form.task.data)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

