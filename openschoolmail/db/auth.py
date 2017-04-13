'''
Created on Apr 13, 2017

@author: robe8437
'''
from openschoolmail.db.models import Staff


def get_user_by_username(db, username):
    staff_member = db.query(Staff).filter(Staff.username == username). \
        filter(Staff.active == True).one()
    return staff_member
