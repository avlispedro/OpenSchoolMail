'''
Created on 4 Mar 2017

@author: Robert Putt
'''
import logging
from flask import Flask
from flask import g
from openschoolmail.config import SECRET_KEY
from openschoolmail.config import DB_URI
from openschoolmail.config import LOG_FILE
from openschoolmail.config import LOG_LEVEL
from openschoolmail.db import get_db_session


APP = Flask(__name__)
APP.secret_key = SECRET_KEY

if LOG_FILE:
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL)
else:
    logging.basicConfig(level=LOG_LEVEL)


@APP.before_request
def before_request():
    if LOG_LEVEL == logging.DEBUG:
        debug = True
    else:
        debug = False
    g.db = get_db_session(DB_URI, debug)


@APP.after_request
def after_request(resp):
    try:
        g.db.close()
    except:
        # Database connection already closed... ignore
        pass
    return resp


def create_app():
    # Register the application blueprints here...

    from openschoolmail.routes.auth import AUTH
    APP.register_blueprint(AUTH)

    return APP


if __name__ == "__main__":
    application = create_app()
    application.run(threaded=True, debug=True)
