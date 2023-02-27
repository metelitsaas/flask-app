from flask import Flask
from main import main as main_blueprint
from api_1_0 import api as api_blueprint


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run()
