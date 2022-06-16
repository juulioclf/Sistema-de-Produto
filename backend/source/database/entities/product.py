from .base import BaseModel
from peewee import PrimaryKeyField, TextField, CharField

class Product(BaseModel):

    id = PrimaryKeyField()
    price = CharField()
    description = TextField()
    category = TextField() 


    def __init__(self, id, price, description, category) -> None:
        self.id = id
        self.price = price
        self.description = description
        self.category = category