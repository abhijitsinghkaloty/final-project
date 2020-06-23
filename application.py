import os

from cs50 import SQL
from flask import Flask, render_template, session, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from tempfile import mkdtemp
from flask_session import Session
from helpers import login_required, credentialCheck, apology

# Setup Flask Server
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Setup database connection
db = SQL("sqlite:///database/kindness.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def home():

    # If Get Request
    if request.method == "GET":
        username = db.execute("SELECT username FROM users WHERE id = :id", session["user_id"])

        return render_template("home.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    LOGIN to the site
    :PARAMS: NONE
    :RETURN: render template, redirect
    """

    # clear session data
    session.clear()

    # If GET request
    if request.method == "GET":
        # Render login.html
        return render_template("login.html")

    # If POST request
    # Data passed to the form
    # Store as variables
    username = request.form.get("username")
    password = request.form.get("password")

    # Returns a TUPLE if something went wrong (ERROR CODE, MESSAGE)
    # Returns an INT that is equal to the user_id in the database
    check = credentialCheck(username, password, True)

    # Returns true if it is a tuple
    state = isinstance(check, tuple)

    if state:
        # Something went wrong
        return apology(check[1], check[0])
    else:
        # Store as a session variable the user id from database
        session["user_id"] = check

    # redirect to homepage
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    REGISTER to the site
    :PARAMS: NONE
    :RETURN: render template, redirect
    """

    # If GET request
    if request.method == "GET":
        # render register.html
        return render_template("register.html")


    # If POST request
    # Data passed to the form
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm")

    check = credentialCheck(username, password, confirm)

    # Returns true if it is a tuple
    state = isinstance(check, tuple)

    if state:
        # Something went wrong
        return apology(check[1], check[0])
      
    # Hash the password
    hashed = generate_password_hash(password)

    """ Store usernme and hash of password to database """
    db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username, hashed)

    # Query database for user_id and store as a session variable
    session["user_id"] = db.execute("SELECT id FROM users WHERE username = :username", username)

    # Redirect to homepage
    return redirect("/")


@app.route("/logout")
def logout():
    """
    LOGOUT account from site
    :PARAMS: NONE
    :RETURN: redirect
    """

    # Clear session data
    session.clear()

    # Redirect homepage
    return redirect("/")
























