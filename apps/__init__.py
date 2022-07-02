from flask import Flask
from .api import api_v1
from conf.config import Config

from models.user import User
from models.transaction import Transaction
from models.wallet import Wallet


def init_app(config=Config, db=None):
    app = Flask(__name__)

    app.config.from_object(config)
    if db:
        db.init_app(app)
    app.register_blueprint(api_v1)

    return app
