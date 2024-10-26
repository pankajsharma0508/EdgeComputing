from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p> Assignment I - Edge Computing By <strong>Group 21!</strong>"


if __name__ == "__main__":
    app.run()
