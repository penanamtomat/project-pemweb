from app import db
from datetime import datetime
from app.model.user_level import user_level

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_user = db.Column(db.String(50))
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False, unique=True)
    id_level_user = db.Column(db.Integer, db.ForeignKey(user_level.id_user_level))
    login_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<User {}>'.format(self.nama_user)