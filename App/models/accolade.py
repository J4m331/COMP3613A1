from App.database import db

class Accolade(db.Model):
    
    accolade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    title = db.Column(db.String(64), nullable = False)
    description = db.Column(db.String(256), nullable = False)
    
    def __init__(self, title, description, student_id):
        self.title = title
        self.description = description
        self.student_id = student_id
        
    def get_json(self):
        return {
            "accolade_id" : self.accolade_id,
            "student_id" : self.student_id,
            "title" : self.title,
            "description" : self.description
        }