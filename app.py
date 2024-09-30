from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

# Criando a aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Definindo o modelo de dados (Base de dados)
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(150), unique=True, nullable=False)

#cRud
@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks = tasks)

# Crud
@app.route('/create', methods=['POST'])
def create_task():
    description = request.form['description']

    # Validar se a trarefa já existe
    existind_task = Tasks.query.filter_by(description = description).first()
    if existind_task:
        return 'Erro: Tarefa já existe!', 400
    new_task = Tasks(description = description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# cruD
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')


# crUd
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        task.description = request.form['description']
        db.session.commit()
    return redirect('/')

# Executando o servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5152)
