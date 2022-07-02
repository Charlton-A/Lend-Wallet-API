from datetime import datetime, timedelta
from flask.json import jsonify, request
from flask.views import MethodView
from models.wallet import Wallet
from middleware.token import token_required


class DateFilterView(MethodView):
    decorators = [token_required]

    def get(self, current_user):
        start_date_obj = (datetime.now() - timedelta(weeks=24)).date(),
        end_date_obj = (datetime.now() + timedelta(weeks=1)).date(),

        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        if start_date:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        wallet = Wallet.query.filter_by(user_id=current_user.id).first()

        profile_data = {
            "user": current_user.user_name,
            "transactions": [
                item.to_json()
                for item in wallet.date_range(start_date_obj, end_date_obj)
            ],
        }
        return jsonify(profile_data)
