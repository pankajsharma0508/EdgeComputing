from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, My Name is <strong>Group 21!</strong>"


if __name__ == "__main__":
    app.run()
