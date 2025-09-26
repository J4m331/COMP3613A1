from App.database import db
from .student import *

def get_hours(student_json):
    return student_json['total_hours']
    

def get_leaderboard():
    students = []
    student_list = get_all_students_json()
    for s in student_list:
        students.append(s)
    
    students.sort(key=get_hours, reverse=True)
    return students
