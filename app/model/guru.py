from app import db
from app.model.user import User

class Guru(db.Model):
    id_guru = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_guru = db.Column(db.String(10), nullable=False)
    nama_guru = db.Column(db.String(50), nullable=False)
    tmpt_lahir_guru = db.Column(db.String(20), nullable=False)
    tgl_lahir_guru = db.Column(db.Date, nullable=False)
    jk_guru = db.Column(db.String(10), nullable=False)
    alamat_guru = db.Column(db.String(100), nullable=False)
    no_hp_guru = db.Column(db.String(15), nullable=False)
    foto_guru = db.Column(db.String(10), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id_user))

    def __repr__(self):
        return '<Guru {}>'.format(self.nama_guru)