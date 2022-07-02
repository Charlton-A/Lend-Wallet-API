from flask import Blueprint
from .views.ping import PingView
from .views.auth import AuthView
from .views.profile import ProfileView
from .views.filter import DateFilterView

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api_v1.add_url_rule('/ping', view_func=PingView.as_view('ping'))
api_v1.add_url_rule('/login', view_func=AuthView.as_view('login'))
api_v1.add_url_rule('/profile', view_func=ProfileView.as_view('profile'))
api_v1.add_url_rule('/filter/date',
                    view_func=DateFilterView.as_view('filter_by_date'))
