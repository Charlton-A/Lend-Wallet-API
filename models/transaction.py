import uuid
from sqlalchemy.dialects.postgresql import UUID
from . import db
from .mixin import TimestampMixin


class Transaction(db.Model, TimestampMixin):
    #TODO : Create transaction_status and transaction_type table
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(
        UUID(as_uuid=True),
        index=True,
        default=uuid.uuid4,
        comment='For use when exposing record to public eg (API)',
    )
    wallet_id = db.Column(db.Integer,
                          db.ForeignKey('wallet.id'),
                          nullable=False)
    txn_type = db.Column(db.Integer)  #1=CREDIT , 2= DEBIT
    status = db.Column(db.Integer)  #1= SUCCESSFUL , 2= PENDING ,3=FAILED
    amount = db.Column(db.Numeric(precision=22, scale=6, asdecimal=True))

    def __init__(self, wallet_id, txn_type, status, amount):
        self.wallet_id = wallet_id
        self.txn_type = txn_type
        self.status = status
        self.amount = amount

    def __repr__(self):
        return f'<Transaction {self.external_id}>'
