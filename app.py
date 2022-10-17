import sys
sys.dont_write_bytecode = True

import flask
from flask import jsonify
from src.routes.users import users
from src.routes.products import products

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify({"Message": "Welcome to the main page"})



app.register_blueprint(users)
app.register_blueprint(products)

app.run(port=80)