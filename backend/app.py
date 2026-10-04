import os

from flask import Flask, render_template, request

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_url_path="",
    static_folder=os.path.join(base_dir, "static"),
    template_folder=os.path.join(base_dir, "templates"),
)


@app.route("/")
def index():
    return app.send_static_file("index.html")


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
        "madlib.html",
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
