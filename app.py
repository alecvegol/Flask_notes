from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    #this creates separate session for each user and it stays after the server shuts
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", notes=notes)
