from app import db

class Guru(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nog = db.Column(db.String(5), unique=True)
    nama_guru = db.Column(db.String(50), nullable=False)
    tmpt_lahir_guru = db.Column(db.String(20), nullable=False)
    tgl_lahir_guru = db.Column(db.Date(20), nullable=False)
    alamat_guru = db.Column(db.String(100), nullable=False)
    no_hp_guru = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Guru {}>'.format(self.nama_guru)