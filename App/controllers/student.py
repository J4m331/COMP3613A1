from App.models import Student, Request, Accolade
from App.database import db

def create_student(username, password, firstname, lastname):
    new_student = Student(username=username, password=password, firstname=firstname, lastname=lastname)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_student(id):
    return db.session.get(Student, id)

def get_all_students():
    return db.session.scalars(db.select(Student)).all()

def get_all_students_json():
    students = get_all_students()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students

def update_student(id, username):
    student = get_student(id)
    if student:
        student.username = username
        db.session.commit()
        return True
    return None

def create_request(id, hours):
    student = get_student(id)
    request = Request(student_id=id,student_firstname=student.firstname,student_lastname=student.lastname,hours= hours)
    db.session.add(request)
    db.session.commit()
    return request

def add_accolade(id):
    student = get_student(id)
    if student:
        hours = student.total_hours
        if hours >= 100:
            existing_accolade = Accolade.query.filter_by(
                title="100 hour Samaritan", 
                student_id=id
            ).first()
            
            if not existing_accolade:
                accolade = Accolade(
                    student_id=id,
                    title="100 hour Samaritan",
                    description="Awarded for 100 hours of community service",
                )
                db.session.add(accolade)
                db.session.commit()
                add_accolade(id)
                return accolade
            
        if hours >= 50:
            existing_accolade = Accolade.query.filter_by(
                title="Gold worker", 
                student_id=id
            ).first()
            
            if not existing_accolade:
                accolade = Accolade(
                    student_id=id,
                    title="Gold worker",
                    description="Awarded for 50 hours of community service",
                )
                db.session.add(accolade)
                db.session.commit()
                add_accolade(id)
                return accolade
        
        if hours >= 20:
            existing_accolade = Accolade.query.filter_by(
                title="Silver worker", 
                student_id=id
            ).first()
            
            if not existing_accolade:
                accolade = Accolade(
                    student_id=id,
                    title="Silver worker",
                    description="Awarded for 20 hours of community service",
                )
                db.session.add(accolade)
                db.session.commit()
                add_accolade(id)
                return accolade
            
        if hours >= 10:
            existing_accolade = Accolade.query.filter_by(
                title="Bronze volunteer", 
                student_id=id
            ).first()
            
            if not existing_accolade:
                accolade = Accolade(
                    student_id=id,
                    title="Bronze volunteer",
                    description="Awarded for 10 hours of community service",
                )
                db.session.add(accolade)
                db.session.commit()
                add_accolade(id)
                return accolade
            
        if hours >= 5:
            existing_accolade = Accolade.query.filter_by(
                title="Novice volunteer", 
                student_id=id
            ).first()
            
            if not existing_accolade:
                accolade = Accolade(
                    student_id=id,
                    title="Novice volunteer",
                    description="Awarded for 5 hours of community service",
                )
                db.session.add(accolade)
                db.session.commit()
                add_accolade(id)
                return accolade
    return None

def list_accolades(id):
    accolades = Accolade.query.filter_by(student_id=id).all()
    return [accolade.get_json() for accolade in accolades]