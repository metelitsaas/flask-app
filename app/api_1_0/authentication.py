from flask_httpauth import HTTPBasicAuth
from api_1_0.errors import unauthorized, forbidden

LOGIN = "admin"
PASSWORD = "admin"


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(login, password):
    return login == LOGIN and password == PASSWORD


@auth.error_handler
def auth_error():
    return unauthorized("Invalid credentials")


@auth.login_required
def before_request():
    return forbidden("Unconfirmed user")
