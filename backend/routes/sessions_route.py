from flask import Blueprint, make_response, request, jsonify
from ..controllers import SessionController

session_route = Blueprint('session_route', __name__)


@session_route.post('/login')
def login():
    try:
        session_dict = request.form.to_dict()
        user = SessionController.login(session_dict)
        print(f"user: {user}")
        # response should redirect to main page having set session_token
        res = make_response(user.to_json())
        res.set_cookie("session_token", user.session_token)
        return res
    except Exception as e:
        return jsonify(str(e))


@session_route.post('/logout')
def logout():
    if SessionController.logout():
        res = make_response("Successfully logged out")
        res.delete_cookie("session_token")
        return res
    else:
        return "Not logged in"
    

    
