'''
Created on 4 Mar 2017

@author: Robert Putt
'''
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from openschoolmail.db import BASE


class Student(BASE):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable=False)
    middle_name = Column(String(40), nullable=True)
    last_name = Column(String(40), nullable=False)
    ps_child = relationship("Parent_Student")
    gs_child = relationship("Group_Student")


class Parent(BASE):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    first_name = Column(String(40), nullable=False)
    middle_name = Column(String(40), nullable=True)
    last_name = Column(String(40), nullable=False)
    email = Column(String(60), nullable=False)
    ps_child = relationship("Parent_Student")


class Parent_Student(BASE):
    __tablename__ = 'parent_student'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'), primary_key=True)


class Group(BASE):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(20), nullable=False)
    gs_child = relationship("Group_Student")
    gg_child = relationship("Group_Group")


class Group_Group(BASE):
    __tablename__ = "group_group"
    parent_group = Column(Integer, ForeignKey('group.id'), primary_key=True)
    child_group = Column(Integer, ForeignKey('group.id'), primary_key=True)


class Group_Student(BASE):
    __tablename__ = 'group_student'
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)


class Staff(BASE):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(250), nullable=False)
    title = Column(String(20), nullable=False)
    first_name = Column(String(40), nullable=False)
    middle_name = Column(String(40), nullable=True)
    last_name = Column(String(40), nullable=False)
    active = Column(Boolean, nullable=False)
    admin = Column(Boolean, nullable=False)
