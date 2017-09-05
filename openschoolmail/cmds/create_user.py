'''
Created on 4 Mar 2017

@author: Robert Putt
'''
import logging
import argparse
import random
import bcrypt
from openschoolmail.config import DB_URI
from openschoolmail.config import SECRET_KEY
from openschoolmail.db.models import Staff
from openschoolmail.db import get_db_session


logging.basicConfig(level=logging.DEBUG)


def generate_password(pw_length=8):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!&^%/+-"
    passwd = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        passwd = passwd + alphabet[next_index]

    return passwd


def add_user():
    desc = 'Add new user to OpenSchoolMail'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('username', help='Desired username for user')
    parser.add_argument('email', help='User\'s email address')
    parser.add_argument('title', help='User\'s preferred title')
    parser.add_argument('first_name', help='User\'s first name')
    parser.add_argument('last_name', help='User\'s last name')
    parser.add_argument('--active',
                        help='Sets the users status to active',
                        action='store_true')
    parser.add_argument('--admin',
                        help='Gives the user administrative privileges',
                        action='store_true')
    args = parser.parse_args()

    logging.info("Adding new user %s" % args.username)
    db = get_db_session(DB_URI, True)

    logging.info("Performing sanity checks")
    existing_staff = db.query(Staff).filter(Staff.username == args.username)
    for staff in existing_staff:
        logging.error("A user with this username already exists, exiting.")
        return        

    if args.admin:
        is_admin = True
    else:
        is_admin = False

    if args.active:
        is_active = True
    else:
        is_active = False

    password = generate_password(8)
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_staff = Staff(username=args.username,
                      email=args.email,
                      password=hashed_pw,
                      title=args.title,
                      first_name=args.first_name,
                      last_name=args.last_name,
                      active=is_active,
                      admin=is_admin)

    db.add(new_staff)
    db.commit()
    logging.info("Added new user %s" % args.username)
    logging.info("Please provide the user with the following temporary "
                 "password to login")
    logging.info("User's Password: %s" % password)

if __name__ == "__main__":
    add_user()
