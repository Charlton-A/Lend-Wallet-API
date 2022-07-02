import uuid
from . import db
from .mixin import TimestampMixin


class Transaction(db.Model, TimestampMixin):
    #TODO : Create transaction_status ,transaction_type,transaction_origin  table
    #TODO :Create enum types for origin, statusm txn_type for readability

    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)

    external_id = db.Column(
        db.String(150),
        index=True,
        default=uuid.uuid4,
        comment='For use when exposing record to public eg (API)',
    )
    wallet_id = db.Column(db.Integer,
                          db.ForeignKey('wallet.id'),
                          nullable=False)
    name = db.Column(db.String(200))
    txn_type = db.Column(db.Integer)  #1=CREDIT , 2= DEBIT
    status = db.Column(db.Integer)  #1= SUCCESSFUL , 2= PENDING ,3=FAILED
    provider = db.Column(db.Integer)  #1= BANK , 2= MOBILE
    amount = db.Column(db.Numeric(precision=22, scale=6, asdecimal=True))

    def __init__(self, wallet_id, txn_type, status, amount, name, provider):
        self.wallet_id = wallet_id
        self.txn_type = txn_type
        self.status = status
        self.amount = amount
        self.name = name
        self.provider = provider

    def to_json(self):
        json_transactions = {
            "external_id": self.external_id,
            "provider": self.provider,
            "amount": self.amount,
            "txn_type": self.txn_type,
            "name": self.name,
            "created_at": self.created_at,
        }
        return json_transactions

    def __repr__(self):
        return f'<Transaction {self.external_id}>'
