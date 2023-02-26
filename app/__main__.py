from flask import Flask
from app.main import main as main_blueprint
from app.api_1_0 import api as api_blueprint


def main():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    app.run(debug=True)


if __name__ == "__main__":
    main()
