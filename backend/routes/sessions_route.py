import json
from flask import Blueprint, make_response, request, jsonify
from ..controllers import SessionController
# from ..db.models.exceptions import UserModelError

session_route = Blueprint('session_route', __name__)


@session_route.post('/login')
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        user = SessionController.login(username, password)
        print("SUCCESS")
        return jsonify(user.id)
    except Exception as e:
        return jsonify(e.message)


@session_route.post('/logout')
def logout():
    SessionController.logout()
