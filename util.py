from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from flask import redirect, session, render
from cs50 import SQL

db = SQL("sqlite:///database/kindness.db")


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


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def credentialCheck(username, password, confirmation):
	"""
	Checks if the user gave the required information for login/register
	PARAMS: username := STR, password := STR, confirmation := STR/BOOL 
	RETURN: INT / (ERROR CODE, MESSAGE)
	CONFIRMATION IS STR := register
	CONFIRMATION IS BOOL := login
	RETURN USER_ID IF REQUIRED INFORMATION WAS GIVEN IF LOGIN
	RETURN TRUE FOR REGISTER IF REQUIRED INFORMATION WAS GIVEN
	"""
	
	# CHECK IF CONFIRMATION IS BOOL
	# TRUE: IF IT'S LOGIN
	if confirmation:

		# Query database of user data
		data = db.execute("SELECT * FROM users WHERE username = :username", username)

		# Check if data has record of username
		# Check if password is valid
		if not data or not check_password_hash(data[0]["hash"], password):
			# Wrong Credentials Display error message
			return (404, "INVALID USERNAME OR PASSWORD")
		
		return data[0]["id"]


	# IF CONFIRMATION STR
	# THEN IT'S REGISTER

	# Check username for validity
	if not username:
		return (404, "PLEASE ENTER USERNAME")

	elif db.execute("SELECT * FROM users WHERE username = :username", username):
		# Username unavailable
        # DISPLAY ERROR MESSAGE
		return (403, "USERNAME ALREADY TAKEN")

	# Check password and password confirmation for validity
	if not password:
        # No password was entered
        # DISPLAY ERROR MESSAGE
		return (404, "PLEASE ENTER PASSWORD")
	
	elif not confirmation:
		# No password confirmation was entered
		# DISPLAY ERROR MESSAGE
		return (404, "PLEASE CONFIRM PASSWORD")

	elif not password == confirmation:
		# Password and Password Confirmation are not equal
		# DISPLAY ERROR MESSAGE
		return (404, "PASSWORD AND PASSWORD CONFIRMATION ARE NOT THE SAME")

	# RETURN TRUE if ALL IS WELL
	return True