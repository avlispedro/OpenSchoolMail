'''
Created on 4 Mar 2017

@author: Robert Putt
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Import are out of order here to stop cyclic imports.
BASE = declarative_base()
from openschoolmail.db.models import Student
from openschoolmail.db.models import Parent
from openschoolmail.db.models import Parent_Student
from openschoolmail.db.models import Group
from openschoolmail.db.models import Group_Student
from openschoolmail.db.models import Staff


def get_db_engine(conn_str, debug=False):
    engine = create_engine(conn_str, echo=debug)
    return engine


def get_db_session(conn_str, debug=False):
    sessmaker = sessionmaker(bind=get_db_engine(conn_str, debug))
    session = sessmaker()
    return session
