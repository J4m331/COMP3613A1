from App.models import Staff, Request, Student
from App.database import db

def create_staff(username, password, firstname, lastname):
    new_staff = Staff(username=username, password=password, firstname=firstname, lastname=lastname)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff

def get_staff(id):
    return db.session.get(Staff, id)

def update_staff(id, username):
    staff = get_staff(id)
    if staff:
        staff.username = username
        db.session.commit()
        return True
    return None

def list_requests():
    requests = db.session.scalars(db.select(Request)).all()
    return requests

def get_request(request_id):
    return db.session.get(Request, request_id)

def get_student(id):
    return db.session.get(Student, id)

def approve_request(request_id):
    request = get_request(request_id)
    student = get_student(request.student_id)
    student.total_hours += request.hours
    db.session.delete(request)
    db.session.commit()
    return True

def deny_request(request_id):
    request = get_request(request_id)
    db.session.delete(request)
    db.session.commit()
    return True

def log_hours(student_id, hours):
    student = get_student(student_id)
    student.total_hours += hours
    return True