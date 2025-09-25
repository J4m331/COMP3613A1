from App.database import db

class Request(db.Model):
    
    request_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    
    def __init__(self, student_id, student_firstname, student_lastname, hours):
        self.student_id = student_id
        self.student_firstname = student_firstname
        self.student_lastname = student_lastname
        self.hours = hours
        
    def get_json(self):
        return {
            'request_id' : self.request_id,
            'student_id' : self.student_id,
            'hours' : self.hours
        }