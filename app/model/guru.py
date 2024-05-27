from app import db

class Guru(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nog = db.Column(db.String(5), unique=True)
    nama_guru = db.Column(db.String(50))

    def __repr__(self):
        return '<Guru {}>'.format(self.username)