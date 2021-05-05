from amazon.database import (db, Model, Column)


class Product(Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'
