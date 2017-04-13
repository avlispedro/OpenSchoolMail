'''
Created on Apr 13, 2017

@author: robe8437
'''

from flask import Blueprint

AUTH = Blueprint("auth", __name__)


@AUTH.route('/login')
def login_form():
    return "Hello"
