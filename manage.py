from flask.cli import FlaskGroup
from faker import Faker
from werkzeug.security import generate_password_hash
from random import randint
from apps import init_app
from conf import ProductionConfig
from models import db
from models.user import User
from models.wallet import Wallet
from models.transaction import Transaction

app = create_app = init_app(config=ProductionConfig, db=db)
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    fake = Faker()

    db.session.add(
        User(email="test@lend-wallet.test",
             user_name="test_user",
             password=generate_password_hash("test")))

    db.session.add(Wallet(user_id=1, currency="KES", balance=90000.50))
    for item in range(1, 11):
        db.session.add(
            Transaction(
                wallet_id=1,
                txn_type=randint(1, 2),
                status=randint(1, 3),
                amount=fake.pyfloat(positive=True, max_value=7000),
            ))

    db.session.commit()


if __name__ == "__main__":
    cli()