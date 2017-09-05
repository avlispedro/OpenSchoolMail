'''
Created on 4 Mar 2017

@author: Robert Putt
'''

# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages
import os

base_name='openschoolmail'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=base_name,
    version='0.1.dev',
    author=u'British Open Educational Software Group',
    author_email='boesg.org.uk',
    include_package_data = True,
    packages=find_packages(), # include all packages under this directory
    description='to update',
    long_description="",
    zip_safe=False,

    # Adds dependencies
    install_requires = ['flask',
                        'sqlalchemy',
                        'pymysql',
                        'bcrypt',
                        'alembic',
                        'argparse']
)

