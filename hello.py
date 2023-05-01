from flask import Flask, url_for, request, make_response, session
from flask.templating import render_template
from markupsafe import escape
from werkzeug.utils import redirect

app = Flask(__name__)

# This realy secret key. Please make sure you dont see it and forgot about that
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
app.secret_key = SECRET_KEY


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404

@app.route("/")
# def index()
#     if "username" in session:
#         app.logger.debug('Log In')
#         # return f"Logged in as {session["username"]}"
#     app.logger.error("You are not logged in")
#     return "You are not logged in"

def hello_world():
    return "<p>Hello, Farmer!</p>"


@app.route("/me")
def me_api():
    app.logger.debug("Return API")
    return {
        "username": "Ak",
        "pigs_in_own": 16,
    }


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        session["username"] = request.form["username"]
        app.logger.debug("Return API")
        return redirect(url_for("index"))
    else:
        app.logger.error("Not login")
        return "Not login page"


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/uploads/uploaded_file.txt")

    return "file"


@app.route("/user/<username>")
def profile(username):
    return f"{username}\'s profile"


with app.test_request_context():
    print(url_for("login"))
    print(url_for("login", next='/'))
    print(url_for("profile", username="Jose"))
