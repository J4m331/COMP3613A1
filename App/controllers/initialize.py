#from .user import create_user
from .student import create_student
from .staff import create_staff
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    #create_user('bob', 'bobpass')
    create_student('bro1', 'abc', 'Jim', 'Doe')
    create_student('bro2', 'abc', 'Jon', 'Doe')
    create_student('bro3', 'abc', 'Jan', 'Doe')
    create_staff('s1', 'eee', 'Overseer', 'Smith')
