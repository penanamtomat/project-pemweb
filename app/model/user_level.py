from app import db

class user_level(db.Model):
    id_user_level = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_level = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<user_level {}>'.format(self.nama_level)