from flask import Flask 
from .source.database.initializer import init_db


app = Flask(__name__)
init_db()

@app.route("/get")
def hello_world():
    return 'teste get'

if __name__ == "__main__":
    app.run()

    