'''
Created on Apr 13, 2017

@author: robe8437
'''
import bcrypt
import logging
from flask import Blueprint
from flask import request
from flask import g
from flask import session
from flask import redirect
from flask.templating import render_template
from openschoolmail.db.auth import get_user_by_username
from sqlalchemy.orm.exc import NoResultFound


AUTH = Blueprint("auth", __name__)


@AUTH.route('/logout')
def logout():
    session['logged_in'] = False
    session['user_id'] = None
    msg = ("You have successfully logged out.")
    return render_template("login.html", msg=msg)


@AUTH.route('/login', methods=["GET"])
def login_form():
    return render_template("login.html")


@AUTH.route('/login', methods=["POST"])
def do_login():
    # Get the username and password from the form.
    username = request.form.get('txt_username', None)
    password = request.form.get('txt_password', None)

    # Check both fields are actually complete.
    if (username is None) or (password is None) \
        or (username == "") or (password == ""):
        # One of the required fields is blank, send the user a message to
        # provide assistance.
        logging.warn("Failed login attempt with username: %s" % username)
        msg = ("Login Failed: Either the username or the password field was "
               "was blank, both fields are required for login.")
        return render_template("login.html", msg=msg)

    try:
        user = get_user_by_username(g.db, username)
    except NoResultFound:
        logging.warn("Failed login attempt with username: %s" % username)
        msg = ("Login Failed: The credentials provided do not appear to "
               "be valid, please re-enter your login details and try again.")
        return render_template("login.html", msg=msg)

    # Encode the credentials before comparing hashes via bcrypt.
    user_hash = user.password.encode('utf-8')
    passwd = password.encode('utf-8')

    if user_hash == bcrypt.hashpw(passwd, user_hash):
        # The hash comparison succeeds suggests the password matches that of
        # the user, login should continue.
        session['logged_in'] = True
        session['user_id'] = user.id
        logging.info("Login Successful: Session created for username: %s"
                     % username)
        return redirect('/')

    else:
        # If the hash comparison fails the user's password is incorrect ==
        # login failed.
        logging.warn("Failed login attempt (incorrect password) "
                     "for username: %s" % username)
        msg = ("Login Failed: The credentials provided do not appear to "
               "be valid, please re-enter your login details and try again.")
        return render_template("login.html", msg=msg)
