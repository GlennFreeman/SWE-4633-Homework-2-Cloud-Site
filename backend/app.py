import os

from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, session, url_for

load_dotenv()

import db

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_url_path="",
    static_folder=os.path.join(base_dir, "static"),
    template_folder=os.path.join(base_dir, "templates"),
)

app.secret_key = os.environ["FLASK_SECRET_KEY"]

oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

MADLIB_FIELDS = (
    [f"adjective{i}" for i in range(1, 5)]
    + [f"adverb{i}" for i in range(1, 4)]
    + [f"noun{i}" for i in range(1, 9)]
    + [f"verb{i}" for i in range(1, 6)]
)


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html.j2", user=user)


@app.route("/login")
def login():
    redirect_uri = url_for("auth_callback", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/auth/callback")
def auth_callback():
    token = google.authorize_access_token()
    user_info = token.get("userinfo")
    if user_info:
        session["user"] = user_info
        session["user_id"] = db.upsert_user(
            google_sub=user_info["sub"],
            email=user_info.get("email"),
            name=user_info.get("name"),
        )
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect("/")


@app.route("/madlib", methods=["GET"])
def madlib():
    words = {field: request.args.get(field) for field in MADLIB_FIELDS}

    user_id = session.get("user_id")
    if user_id and all(words.values()):
        new_id = db.save_madlib(user_id, words)
        # Redirect so refreshing the page doesn't save a duplicate.
        return redirect(url_for("saved_madlib", madlib_id=new_id))

    return render_template("madlib.html.j2", **words)


@app.route("/madlib/<int:madlib_id>")
def saved_madlib(madlib_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    words = db.get_madlib(user_id, madlib_id)
    if words is None:
        abort(404)
    return render_template("madlib.html.j2", **words)


@app.route("/history")
def history():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    return render_template(
        "history.html.j2", user=session.get("user"), madlibs=db.list_madlibs(user_id)
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
