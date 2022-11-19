from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_migrate import Migrate
from database import db
from models.models import Itens

app = Flask (__name__)
db.init_app(app)
conexao = 'sqlite:///database.db'

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



migrate = Migrate(app, db)

@app.route('/')
def index():
    dados = Itens.query.all()
    return render_template('index.html', itens = dados)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        situação = request.form['situacao']
        descrição = request.form['descricao']
        item = request.form['item']
        codigo_item = request.form['codigo_item']

        novo_item = Itens(situação=situação, descrição=descrição, item=item, codigo_item=codigo_item)

        db.session.add(novo_item)
        db.session.commit()

        flash (f'Item {item} cadastrado com sucesso', category='soccess')

        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    
    if request.method == 'POST':
        edit_item = Itens.query.get(request.form['id'])
        
        edit_item.situação = request.form['situacao']        
        edit_item.descrição = request.form['descricao']
        edit_item.item = request.form['item']
        edit_item.codigo_item = request.form['codigo_item']

        db.session.commit()
        
        flash (f'Item editado com sucesso', category='soccess')

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)