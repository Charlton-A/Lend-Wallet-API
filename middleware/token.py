from flask import  request, jsonify
import jwt
from models.user import User
import os
from flask import  g

from functools import wraps

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "X-LEND-TOKEN" in request.headers:
            token = request.headers["X-LEND-TOKEN"]

        if not token:
            return jsonify({'message': 'a valid token is missing'}),401

        try:
            data = jwt.decode(token,
                              os.environ["APP_KEY"],
                              algorithms=["HS256"],
                            )
            current_user = User.query.filter_by(
                external_id=data["external_id"]).first()

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "token expired"}),401

        except (jwt.InvalidSignatureError ,jwt.InvalidTokenError):
            return jsonify({"message": "token is invalid"}),401

        except Exception as e:
            return jsonify({"message": "internal server error"}),500

        return f(current_user, *args, **kwargs)
    return decorator
