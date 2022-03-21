from flask import Blueprint, make_response, request, jsonify
from ..controllers import SessionController

session_route = Blueprint('session_route', __name__)


@session_route.post('/login')
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    # print(username, password)
    logged_in = SessionController.login(username, password)
    return jsonify(logged_in)