from flask import Flask, render_template, flash, redirect, url_for, request, session

from database import db, app
from models.models import Itens



@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    dados = Itens.query.paginate(page=page,per_page=10)
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
        edit_item = Itens.query.get(request.form.get('id'))
        
        edit_item.situação = request.form['situacao']        
        edit_item.descrição = request.form['descricao']
        edit_item.item = request.form['item']
        edit_item.codigo_item = request.form['codigo_item']

        db.session.commit()
        
        flash (f'Item editado com sucesso', category='soccess')

        return redirect(url_for('index'))

@app.route('/search', methods = ['GET','POST'])
def search(results=None):
    if request.method == 'POST':
        results = Itens.query.filter_by(request.form.get('search')).all()
    return redirect(url_for('index', results = results))


if __name__ == "__main__":
    app.run(debug=True)