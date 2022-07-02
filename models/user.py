from sqlalchemy.dialects.postgresql import UUID
from .mixin import TimestampMixin
import uuid
from . import db


class User(db.Model, TimestampMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(
        UUID(as_uuid=True),
        index=True,
        default=uuid.uuid4,
        comment='For use when exposing record to public eg (API)',
    )
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150))
    is_active = db.Column(db.Boolean, unique=False, default=True)
    wallets = db.relationship('Wallet',
                              lazy='select',
                              backref=db.backref('user', lazy='joined'))

    def __init__(self, user_name, email, password):
        self.email = email
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return f'<User {self.user_name}>'
