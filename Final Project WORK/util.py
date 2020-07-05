from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from flask import redirect, session, render_template
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


def apology():

    return render_template("apology.html")


def credentialCheck(username, password, confirmation):
	"""
	Checks if the user gave the required information for login/register
	PARAMS: username := STR, password := STR, confirmation := STR/BOOL 
	RETURN: INT / BOOL
	CONFIRMATION IS STR := register
	CONFIRMATION IS BOOL := login
	RETURN USER_ID IF REQUIRED INFORMATION WAS GIVEN IF LOGIN
	RETURN TRUE IF ALL IS WELL / REGISTER
	RETURN FALSE WHEN SOMETHING WENT WRONG
	"""
	
	# CHECK IF CONFIRMATION IS BOOL
	# TRUE: IF IT'S LOGIN
	if confirmation:

		# Query database of user data
		data = db.execute("SELECT * FROM users WHERE username = :username", username)

		# Check if data has record of username, check password if valid
		if not data or not check_password_hash(data[0]["hash"], password):
			# Wrong Credentials Display error message
			return False
		
		# Return user_id
		return data[0]["id"]


	# IF CONFIRMATION STR
	# THEN IT'S REGISTER

	# Check username for validity
	if not username:
		return False

	elif db.execute("SELECT * FROM users WHERE username = :username", username):
		# Username unavailable
		return False

	# Check password and password confirmation for validity
	if not password:
        # No password was entered
		return False
	
	elif not confirmation:
		# No password confirmation was entered
		return False

	elif not password == confirmation:
		# Password and Password Confirmation are not equal
		return False

	# RETURN TRUE if ALL IS WELL
	return True