from flask import Flask

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/madlib/index.html", methods=["POST"])
def madlib():
    return app.send_static_file("/madlib/index.html")
