import os

from authlib.integrations.flask_client import OAuth
from flask import Flask, render_template, request, session, url_for

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
    server_metadata_url="https://google.com",
    client_kwargs={"scope": "openid email profile"},
)


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html.j2", user=user)


@app.route("/login")
def login():
    # Redirects to Google's OAuth consent screen
    redirect_uri = url_for("auth_callback", _external=True)
    return google.authorize_redirect(redirect_uri)


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
