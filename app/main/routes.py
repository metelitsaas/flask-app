from main import main


@main.route("/")
def index():
    return "Test Flask server"
