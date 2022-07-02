from http.client import IM_USED
import pytest
from apps import init_app
from conf import DevelopmentConfig
from models.user import User
from models.wallet import Wallet
from models.transaction import Transaction


@pytest.fixture()
def app():
    app = init_app(DevelopmentConfig)
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.mark.unit
def test_user(client):
    user = User(
        user_name="Rick_Sanchez",
        email="ricksanchez@c137.com",
        password="WubbLubbaDub-Dub",
    )
    assert user.email == 'ricksanchez@c137.com'
    assert user.user_name == 'Rick_Sanchez'
    assert user.password == 'WubbLubbaDub-Dub'


@pytest.mark.unit
def test_wallet(client):
    wallet = Wallet(
        user_id=1,
        currency="KES",
        balance=8000.45,
    )
    assert wallet.user_id == 1
    assert wallet.currency == 'KES'
    assert wallet.balance == 8000.45


@pytest.mark.unit
def test_transaction(client):
    txn = Transaction(
        wallet_id=1,
        txn_type=1,
        status=2,
        amount=8001.45,
        provider=1,
        name="morty@c137.com",
    )
    assert txn.wallet_id == 1
    assert txn.txn_type == 1
    assert txn.status == 2
    assert txn.amount == 8001.45
    assert txn.name == "morty@c137.com"
    assert txn.provider == 1
