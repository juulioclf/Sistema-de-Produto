from peewee import SqliteDatabase
from .source.database.entities.product import Product

def init_db():
    db = SqliteDatabase("database.db")

    db.connect()
    db.create_tables([Product])