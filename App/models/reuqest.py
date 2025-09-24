from App.database import db

class Request(db.Model):
    
    request_id = db.Column(db.Integer, primary_key=True)
    student_id = db.relationship('Student',backref="request",lazy=True)
    student_name = db.Column(db.String(20), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    
    def __init__(self, student_id, student_name, hours):
        self.student_id = student_id
        self.student_name = student_name
        self.hours = hours
        
    def get_json(self):
        return {
            'request_id' : self.request_id,
            'student_id' : self.student_id,
            'student_name' : self.student_name,
            'hours' : self.hours
        }