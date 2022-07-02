from asyncio.trsock import TransportSocket
from sqlalchemy.dialects.postgresql import UUID
import uuid

from models.transaction import Transaction

from sqlalchemy import desc
from sqlalchemy.ext.serializer import loads, dumps
from .mixin import TimestampMixin
from . import db


class Wallet(db.Model, TimestampMixin):
    __tablename__ = 'wallet'
    __table_args__ = (db.CheckConstraint(
        'balance >= 0', name='wallet balance cannot be less than 0'),)
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(
        db.String(150),
        index=True,
        default=uuid.uuid4,
        comment='For use when exposing record to public eg (API)',
    )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    currency = db.Column(db.String(5))
    balance = db.Column(db.Numeric(precision=22, scale=6, asdecimal=True))
    transactions = db.relationship('Transaction',
                                   lazy='select',
                                   backref=db.backref('wallet', lazy='joined'))

    def __init__(self, user_id, currency, balance):
        self.user_id = user_id
        self.currency = currency
        self.balance = balance

    def __repr__(self):
        return f'<Wallet {self.external_id}>'