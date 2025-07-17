from flask import Flask, render_template
from flask import url_for, request, flash

from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user
from flask import session, redirect
import sqlite3


from modelos import User

DATABASE='banco.sql'
conn = sqlite3.connect('banco.db')

with open(DATABASE) as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

login_manager = LoginManager() 
app = Flask(__name__)
app.secret_key = 'guilherme'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    if 'usuarios' not in session:
        usuarios = {}
        session['usuarios'] = usuarios
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        # pegar os dados do usuário
        email = request.form['email']
        senha= request.form['senha']

        # verificar a senha se existir o usuário
        l_usuarios = session.get('usuarios')
        if email in l_usuarios and senha == l_usuarios[email]: 
            user = User(nome=email, senha=senha)
            user.id = email
            login_user(user)
            return redirect(url_for('dash'))

        flash('Houve errro: senha ou login inválidos.', category='error')
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        email = request.form['email']
        senha= request.form['senha']
        #check
        usuarios = session.get('usuarios')
        if email not in usuarios.keys():
            usuarios[email] = senha
            session['usuarios'] = usuarios
            # logar
            user = User(email, senha)
            user.id = email
            print(usuarios)
            login_user(user)
            return redirect(url_for('dash'))

        flash('Erro ao realizar cadastro', category='error')
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/dash')
@login_required
def dash():
    return render_template('dashboard.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():

    logout_user()

    return redirect(url_for('index'))