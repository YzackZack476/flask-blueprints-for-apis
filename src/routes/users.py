import flask
from flask import jsonify

users = flask.Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def users_home():
    return jsonify({"Message": "There is no users"})
