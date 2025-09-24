from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from user import User

class Staff(User):
    
    pending_requests = db.relationship('Request', backref='staff', lazy = True)
    
    def __init__(self, username, password):
        super().__init__(username, password)
        
    def get_json(self):
        return{
            'id': super.id,
            'username': super.username
        }