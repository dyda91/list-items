from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, current_user
from config import app, db, bcrypt
from models.forms import LoginForm, RegisterForm
from models.models import Itens, User





@app.route('/', methods = ['GET','POST'])
def index():
    if not current_user.is_authenticated:
         return redirect( url_for('login'))
    page = request.args.get('page', 1, type=int)
    dados = Itens.query.paginate(page=page,per_page=10) 
    return render_template('index.html', itens = dados)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        user_username = current_user.username
        situação = request.form['situacao']
        descrição = request.form['descricao']
        item = request.form['item']
        codigo_item = request.form['codigo_item']

        novo_item = Itens(user_username=user_username, situação=situação, descrição=descrição, item=item, codigo_item=codigo_item)

        db.session.add(novo_item)
        db.session.commit()

        flash (f'Item {item} cadastrado com sucesso', category='soccess')

        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    
    if request.method == 'POST':
        edit_item = Itens.query.get(request.form.get('id'))
        
        edit_item.situação = request.form['situacao']        
        edit_item.descrição = request.form['descricao']
        edit_item.item = request.form['item']
        edit_item.codigo_item = request.form['codigo_item']

        db.session.commit()
        
        flash (f'Item editado com sucesso', category='soccess')

        return redirect(url_for('index'))
        

@app.route('/busca', methods=['GET', 'POST'])
def busca():
    if request.method == 'POST':

        busca = Itens.query.filter_by(item = request.form.get('search')).all()

        return render_template('search.html', busca = busca)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    item = Itens.query.get(id)

    db.session.delete(item)
    db.session.commit()

    flash (f'Item deletado com sucesso', category='soccess')

    return redirect(url_for('index'))



### Autenticação ###

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('logged'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        logged_user = form.username.data
        session["logged_user"] = logged_user

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("logged"))
        else:
            flash(f'Erro ao logar no usuário {form.username.data}', category='danger')
    return render_template('login.html', form=form)  

##Sessão##

@app.route("/logged")
def logged():
    if "logged_user" in session:
        logged_user = session["logged_user"]
        return redirect(url_for('index'))
    else:
        return redirect(url_for("login"))

##logout##

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))        

##  Register ##

@app.route('/register', methods=["POST", "GET"])
def signin():
    form = RegisterForm() 
    if current_user.is_authenticated:
         return redirect( url_for('index'))
    if form.validate_on_submit(): 

        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        new_user = User(username=form.username.data, password=encrypted_password, name=form.name.data)  

        db.session.add(new_user)
        db.session.commit() 

        flash(f'Conta criada com socesso para o usuário {form.username.data}', category='success')

        return redirect(url_for('login'))
    return render_template('signin.html', form=form)


@app.route('/teste')
def teste():
    novo_item = Itens(user_username=current_user.username, situação='situação', descrição='descrição', item='item', codigo_item='codigo_item')
    db.session.add(novo_item)
    db.session.commit() 
    return('sucesso')


if __name__ == "__main__":
    app.run(debug=True)