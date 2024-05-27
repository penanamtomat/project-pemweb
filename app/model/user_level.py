from app import db

class user_level(db.Model):
    id_level_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_level = db.Column(db.String(10))

    def __repr__(self):
        return '<user_level {}>'.format(self.nama_level)