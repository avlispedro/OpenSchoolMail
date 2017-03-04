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


def get_db_engine(conn_str, debug=False):
    engine = create_engine(conn_str, echo=DEBUG)
    return engine


def get_db_session(conn_str, debug=False):
    session = sessionmaker()
    session.configure(bind=get_db_engine(conn_str, debug))
    return session


def init_db(conn_str, debug=True):
    BASE.metadata.create_all(get_db_engine(conn_str, debug))
