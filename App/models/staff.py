from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from user import User

class Staff(User):
    
    pending_requests = db.relationship('Request', backref='staff', lazy = True)
    
    def __init__(self, username, password, firstname, lastname):
        super().__init__(username, password, firstname, lastname)
        
    def get_json(self):
        return{
            'id': super.id,
            'username': super.username,
            'firstname': super.firstname,
            'lastname': super.lastname
        }