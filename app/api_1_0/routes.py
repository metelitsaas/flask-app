from flask import jsonify
from api_1_0 import api
from api_1_0.authentication import auth


@api.route("/")
def index():
    return "API v1"


@api.route("/test_data/")
@auth.login_required
def get_test_data():
    return jsonify({
        "test_key_1": "test_value_1",
        "test_key_2": "test_value_2",
        "test_key_3": "test_value_3"
    })
