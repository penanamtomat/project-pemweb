from app import db
from app.model.user_level import user_level
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_user = db.Column(db.String(50))
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=True)
    id_level_user = db.Column(db.Integer, db.ForeignKey(user_level.id_user_level))

    def __repr__(self):
        return '<User {}>'.format(self.nama_user)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)