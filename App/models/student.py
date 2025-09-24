from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from user import User

class Student(User):
    
    total_hours = db.Column(db.Integer, nullable = False)
    accolades = db.relationship('Accolade', backref='student', lazy = True)
    
    def __init__(self, username, password):
        super().__init__(username, password)
        self.total_hours = 0
        
    def get_json(self):
        return{
            'id': super.id,
            'username': super.username,
            'total_hours': self.total_hours
        }