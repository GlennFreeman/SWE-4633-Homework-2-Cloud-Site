import os

from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_url_path="",
    static_folder=os.path.join(base_dir, "static"),
    template_folder=os.path.join(base_dir, "templates"),
)

app.secret_key = os.urandom(24)

oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
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
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


@app.route("/madlib", methods=["GET"])
def madlib():
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    adjective4 = request.args.get("adjective4")

    adverb1 = request.args.get("adverb1")
    adverb2 = request.args.get("adverb2")
    adverb3 = request.args.get("adverb3")

    noun1 = request.args.get("noun1")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("noun3")
    noun4 = request.args.get("noun4")
    noun5 = request.args.get("noun5")
    noun6 = request.args.get("noun6")
    noun7 = request.args.get("noun7")
    noun8 = request.args.get("noun8")

    verb1 = request.args.get("verb1")
    verb2 = request.args.get("verb2")
    verb3 = request.args.get("verb3")
    verb4 = request.args.get("verb4")
    verb5 = request.args.get("verb5")

    return render_template(
        "madlib.html.j2",
        adjective1=adjective1,
        adjective2=adjective2,
        adjective3=adjective3,
        adjective4=adjective4,
        adverb1=adverb1,
        adverb2=adverb2,
        adverb3=adverb3,
        noun1=noun1,
        noun2=noun2,
        noun3=noun3,
        noun4=noun4,
        noun5=noun5,
        noun6=noun6,
        noun7=noun7,
        noun8=noun8,
        verb1=verb1,
        verb2=verb2,
        verb3=verb3,
        verb4=verb4,
        verb5=verb5,
    )


if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run(host="localhost", port=5000, debug=True)
