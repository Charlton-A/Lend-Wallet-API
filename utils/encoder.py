from flask import json
from decimal import Decimal
from uuid import UUID


class CustomJSONEncoder(json.JSONEncoder):

    def default(self, value):
        if isinstance(value, Decimal):
            return str(value)
        if isinstance(value, UUID):
            return str(value)
        return json.JSONEncoder.default(self, value)
