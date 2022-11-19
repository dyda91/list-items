from database import db

class Itens(db.Model):
    __tablename__='itens'
    id = db.Column(db.Integer, primary_key=True)
    situação = db.Column(db.String)
    descrição = db.Column(db.String)
    item = db.Column(db.String)
    codigo_item = db.Column(db.String)

    def __init__(self, situação, descrição, item, codigo_item):
        self.situação = situação
        self.descrição = descrição
        self.item = item
        self.codigo_item = codigo_item

        db.create_all()
        db.session.commit()


    def __repr__(self):
        return 'Item: {}' .format(self.item)