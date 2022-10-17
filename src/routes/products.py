import flask
from flask import jsonify

products = flask.Blueprint('products', __name__)

@products.route('/products', methods=['GET'])
def products_home():
    return jsonify({"Message": "There is no products"})
