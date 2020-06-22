from cs50 import SQL
from flask import Flask, render_template, session, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from tempfile import mkdtemp
from flask_session import Session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash


# Setup Flask Server
app = Flask(__name__)

# Configure session to use filesystem 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Setup database connection
#db = SQL("sqlite3:///databases/project.db")


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@login_required
def home():
    return "HELLO"


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

    # Query database of user data
    data = db.execute("SELECT * FROM users WHERE username = :username", username)

    # Check if data has record of username
    # Check if password is valid
    if not data or not check_password_hash(data[0]["hash"], password):
        # Wrong Credentials Display error message
        pass
    
    # Store as a session variable the user id from database
    session["user_id"] = data[0]["id"]

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
    

    # Check Username for validity
    if not username:
        # No username was entered 
        # DISPLAY ERROR MESSAGE
        pass

    elif db.execute("SELECT * FROM user WHERE username = :username", username):
        # Username unavailable
        # DISPLAY ERROR MESSAGE
        pass

    # Check password and password confirmation for validity
    if not password: 
        # No password was entered
        # DISPLAY ERROR MESSAGE
        pass

    elif not confirm:
        # No password confirmation was entered
        # DISPLAY ERROR MESSAGE
        pass

    elif not password == confirm:
        # Password and Password Confirmation are not equal
        # DISPLAY ERROR MESSAGE
        pass


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


if __name__ == "__main__":
    app.run()

























