from flask.json import jsonify
from flask.views import MethodView
from flask import request, jsonify
import jwt
from models.user import User
import os
import datetime
from werkzeug.security import check_password_hash


class AuthView(MethodView):
    #TODO :Add jwt token refresh and make expiry configurable

    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if not username or not password:
            return jsonify({"Authentication": "login required"}), 401

        user = User.query.filter_by(user_name=username).first()

        if check_password_hash(user.password, password):
            token = jwt.encode(
                {
                    "external_id": str(user.external_id),
                    "exp": datetime.datetime.utcnow() +
                           datetime.timedelta(minutes=60)
                }, os.environ['APP_KEY'], "HS256")
            return jsonify({"token": token})

        return jsonify({"Authentication": "login required"}), 401
