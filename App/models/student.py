from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    total_hours = db.Column(db.Integer, nullable = False)
    accolades = db.relationship('Accolade', backref='student', lazy = True)
    
    __mapper_args__ = {'polymorphic_identity': 'student'}
    
    def __init__(self, username, password, firstname, lastname):
        super().__init__(username, password, firstname, lastname)
        self.total_hours = 0
        
    def get_json(self):
        return{
            'id': super.id,
            'username': super.username,
            'total_hours': self.total_hours
        }