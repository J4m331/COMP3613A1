from App.database import db

class Accolade(db.Model):
    
    title = db.Column(db.String(64), nullable = False)
    description = db.Column(db.String(256), nullable = False)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description