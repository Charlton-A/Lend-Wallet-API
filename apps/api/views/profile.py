from trace import Trace
from flask.json import jsonify
from flask.views import MethodView
from models.wallet import Wallet
from middleware.token import token_required


class ProfileView(MethodView):
    decorators = [token_required]

    def get(self, current_user):
        wallet = Wallet.query.filter_by(user_id=current_user.id).first()

        profile_data = {
            "user": current_user.user_name,
            "balance": wallet.balance,
            "currency": wallet.currency,
        }
        return jsonify(profile_data)
